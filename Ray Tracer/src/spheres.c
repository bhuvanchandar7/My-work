#include <stdio.h>  
#include <stdlib.h>  
#include <math.h>   
#include "spheres.h" 

void worldInit(World *world) {
    world->spheres = NULL;
    world->size = 0;
    world->capacity = 0; 
}

void freeWorld(World *world) {
    for (int i = 0; i < world->size; i++) {
        free(world->spheres[i]);  
    }
    free(world->spheres);  
    world->spheres = NULL;
    world->size = 0;
    world->capacity = 0;
}

void addSphere(World *world, Sphere *sphere) {
    if (world->size == world->capacity) {
        int newCapacity = world->capacity > 0 ? world->capacity * 2 : 1;
        Sphere **newSpheres = realloc(world->spheres, newCapacity * sizeof(Sphere *));
        if (newSpheres == NULL) {
            fprintf(stderr, "Failed to reallocate memory for spheres.\n");
            return; 
        }
        world->spheres = newSpheres;
        world->capacity = newCapacity;
    }
    world->spheres[world->size++] = sphere;
}

Sphere *createSphere(float radius, Vec3 position, Vec3 color) {
    Sphere *newSphere = malloc(sizeof(Sphere));
    if (newSphere == NULL) {
        fprintf(stderr, "Failed to allocate memory for new sphere.\n");
        return NULL;  
    }
    newSphere->r = radius;
    newSphere->pos = position;
    newSphere->color = color;
    return newSphere;
}

int doesIntersect(const Sphere *sphere, Vec3 rayPos, Vec3 rayDir, float *t) {
    Vec3 sphereToRay = subtract(rayPos, sphere->pos);

    float a = dot(rayDir, rayDir);
    float b = 2 * dot(rayDir, sphereToRay);
    float c = dot(sphereToRay, sphereToRay) - sphere->r * sphere->r;

    float discriminant = b * b - (4 * a * c);

    if (discriminant < 0) {
        return 0;
    }

    float t1 = (-b - sqrt(discriminant)) / (2 * a);
    float t2 = (-b + sqrt(discriminant)) / (2 * a);

    if (t1 > 0 && t2 > 0) {
        *t = fmin(t1, t2);
    } else if (t1 > 0) {
        *t = t1;
    } else if (t2 > 0) {
        *t = t2;
    } else {
        return 0;
    }

    return 1;
}