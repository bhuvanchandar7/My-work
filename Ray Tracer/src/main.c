#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "vector.h"
#include "spheres.h"
#include "color.h"

typedef struct {
    Vec3 position;
    float focalLength;
} Camera;

typedef struct {
    float height;
    float width;
    float z;
} Viewport;

Camera camera = {{0, 0, 0}, 0};
Viewport viewport = {0, 0, 0};

void initializeCameraAndViewport(float viewportHeight, float focalLength, int imageWidth, int imageHeight) {
    camera.position = (Vec3){0, 0, 0};
    camera.focalLength = focalLength;
    viewport.height = viewportHeight;
    viewport.width = viewportHeight * ((float)imageWidth / imageHeight);
    viewport.z = -focalLength;
}

Vec3 createRay(int pixelX, int pixelY, int imageWidth, int imageHeight) {
    float vx = (pixelX + 0.5f) * (viewport.width / imageWidth) - viewport.width / 2;
    float vy = (viewport.height / 2) - (pixelY + 0.5f) * (viewport.height / imageHeight);
    Vec3 direction = {vx, vy, viewport.z};
    return normalize(direction);
}

void renderScene(FILE *outputFile, World *world, Vec3 lightPos, float lightIntensity,
                 int imageWidth, int imageHeight, unsigned int *colors, int backgroundColorIndex) {
    fprintf(outputFile, "P3\n%d %d\n255\n", imageWidth, imageHeight);

    Vec3 backgroundColor = unpackRGB(colors[backgroundColorIndex]);

    for (int y = 0; y < imageHeight; y++) {
        for (int x = 0; x < imageWidth; x++) {
            Vec3 rayDir = createRay(x, y, imageWidth, imageHeight);
            float minT = INFINITY;
            Sphere *closestSphere = NULL;

            // Find closest sphere
            for (int i = 0; i < world->size; i++) {
                float t;
                if (doesIntersect(world->spheres[i], camera.position, rayDir, &t) && t < minT) {
                    minT = t;
                    closestSphere = world->spheres[i];
                }
            }

            Vec3 pixelColor = backgroundColor;

            if (closestSphere) {
                Vec3 intersectionPoint = add(camera.position, scalarMultiply(minT, rayDir));
                Vec3 normal = normalize(subtract(intersectionPoint, closestSphere->pos));
                Vec3 lightDir = normalize(subtract(lightPos, intersectionPoint));

                float intensity = lightIntensity * fmax(0, dot(normal, lightDir)) /
                                  length2(subtract(lightPos, intersectionPoint));

                intensity = fmin(1.0f, intensity);

                pixelColor = (Vec3){
                    intensity * closestSphere->color.x,
                    intensity * closestSphere->color.y,
                    intensity * closestSphere->color.z};

                // Shadow calculation
                Vec3 shadowRayOrigin = add(intersectionPoint, scalarMultiply(0.001f, normal));
                for (int i = 0; i < world->size; i++) {
                    float t;
                    if (doesIntersect(world->spheres[i], shadowRayOrigin, lightDir, &t)) {
                        pixelColor = scalarMultiply(0.1f, pixelColor);
                        break;
                    }
                }
            }

            writeColour(outputFile, pixelColor);
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s <input file> <output file>\n", argv[0]);
        return 1;
    }

    FILE *inputFile = fopen(argv[1], "r");
    FILE *outputFile = fopen(argv[2], "w");
    if (!inputFile || !outputFile) {
        fprintf(stderr, "Error opening files: %s or %s\n", argv[1], argv[2]);
        if (inputFile) fclose(inputFile);
        if (outputFile) fclose(outputFile);
        return 1;
    }

    int imageWidth, imageHeight, numColors, backgroundColorIndex, numSpheres;
    float viewportHeight, focalLength, lightIntensity;
    Vec3 lightPos;

    fscanf(inputFile, "%d %d", &imageWidth, &imageHeight);
    fscanf(inputFile, "%f %f", &viewportHeight, &focalLength);
    fscanf(inputFile, "%f %f %f %f", &lightPos.x, &lightPos.y, &lightPos.z, &lightIntensity);
    fscanf(inputFile, "%d", &numColors);

    unsigned int *colors = malloc(numColors * sizeof(unsigned int));
    for (int i = 0; i < numColors; i++) {
        fscanf(inputFile, "%x", &colors[i]);
    }
    qsort(colors, numColors, sizeof(unsigned int), compareColor);

    fscanf(inputFile, "%d", &backgroundColorIndex);

    World world;
    worldInit(&world);
    fscanf(inputFile, "%d", &numSpheres);

    for (int i = 0; i < numSpheres; i++) {
        Vec3 position;
        float radius;
        int colorIndex;
        fscanf(inputFile, "%f %f %f %f %d", &position.x, &position.y, &position.z, &radius, &colorIndex);
        Vec3 sphereColor = unpackRGB(colors[colorIndex]);
        Sphere *newSphere = createSphere(radius, position, sphereColor);
        if (newSphere) addSphere(&world, newSphere);
    }

    initializeCameraAndViewport(viewportHeight, focalLength, imageWidth, imageHeight);
    renderScene(outputFile, &world, lightPos, lightIntensity, imageWidth, imageHeight, colors, backgroundColorIndex);
    freeWorld(&world);
    free(colors);
    fclose(inputFile);
    fclose(outputFile);

    return 0;
}
