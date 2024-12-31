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

    for (int y = 0; y < imageHeight; y++) {
        for (int x = 0; x < imageWidth; x++) {
            Vec3 total_color = {0, 0, 0};
            int aliasing = 3;
        }
        sampleColor = (Vec3){
            intensity * closest_sphere->color.x,
            intensity * closest_sphere->color.y,
            intensity * closest_sphere->color.z};
        sampleColor = unpackRGB(colors[backgroundColorIndex]);

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
    free(world.spheres);
    fclose(inputFile);
    fclose(outputFile);

    return 0;
}
