//
//  main.h
//  vehicle
//
//  Created by VÕ PHAN ANH QUÂN  on 5-11-23.
//

#ifndef main_h
#define main_h

#include <GLUT/glut.h>
#include <math.h>

class Point3D {
public:
    float x, y, z;
    Point3D() {this->x = 0; this->y = 0; this->z = 0;}
    Point3D(float x, float y, float z) {
        this->x = x;
        this->y = y;
        this->z = z;
    }
    
    void set(float dx, float dy, float dz){
        x = dx;
        y = dy;
        z = dz;
    }

};

Point3D faceNorm(Point3D pt1, Point3D pt2, Point3D pt3){
    float v1x = pt2.x - pt1.x;
    float v1y = pt2.y - pt1.y;
    float v1z = pt2.z - pt1.z;

    float v2x = pt3.x - pt1.x;
    float v2y = pt3.y - pt1.y;
    float v2z = pt3.z - pt1.z;

    float nx = v1y * v2z - v1z * v2y;
    float ny = v1z * v2x - v1x * v2z;
    float nz = v1x * v2y - v1y * v2x;

    float length = sqrt((nx) * (nx) + (ny) * (ny) + (nz) * (nz));
    if (length > 0) {
        nx /= length;
        ny /= length;
        nz /= length;
    }

    return Point3D(nx, ny, nz);
    
}


void drawAxis()
{
    glBegin(GL_LINES);
        glColor3f(0, 0, 1);
        glVertex3f(0, 0, 0);
        glVertex3f(16, 0, 0);

        glColor3f(0, 1, 0);
        glVertex3f(0, 0, 0);
        glVertex3f(0, 16, 0);

        glColor3f(1, 0, 0);
        glVertex3f(0, 0, 0);
        glVertex3f(0, 0, 16);
    glEnd();
}





#endif /* main_h */
