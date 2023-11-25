
#define GL_SILENCE_DEPRECATION
#include <GLUT/GLUT.h>
#include <OpenGL/OpenGL.h>
#include <OpenGL/OpenGLAvailability.h>

#include <math.h>
#include <iostream>

#include "main.h"

int    SCREEN_WIDTH = 500;
int    SCREEN_HEIGHT= 500;
float PI = M_PI;
GLenum mode = GL_FILL;
int posX = 50;
int posY = 10;
int posZ = 30;
bool upper_mode = false;

float all_rotate = 0;
float part_rotate = 0;
float second_rotate = 0;
int rotator_rotate = 0;

int first_angle[]= {225, 230, 234, 236, 239, 241, 242, 244, 246, 288, 290, 291,
                    292, 293, 295, 296, 297, 299, 301, 303, 305, 311, 315};
int num_rotate = sizeof(first_angle)/sizeof(int);

int double_rotate[] = {245, 261, 263, 265, 267, 269, 272, 275, 279, 287};
int db_rotate = sizeof(double_rotate)/sizeof(int);

bool is_exist(int array[], int element, int size){
    for (int i = 0; i < size; ++i) {
        if (array[i] == element) return true;
    }
    return false;
}

void setupMaterial(GLfloat ambient[], GLfloat diffuse[], GLfloat specular[]){
    float shiness = 60;
    
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient);
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse);
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular);
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shiness);
}


void Light(GLfloat ambient[], GLfloat new_ambient[], GLfloat diffuseLight[], GLfloat specularLight[]) {
    
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_LIGHT1);
    glEnable(GL_DEPTH_TEST);
    
    GLfloat lightPosition[] = {0.0f, 0.0f, 600.0f, 0.0f};
    GLfloat light1Position[] = {0.0f, 0.0f, -600.0f, 0.0f};
    
    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition);
    glLightfv(GL_LIGHT1, GL_POSITION, light1Position);

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight);
    glLightfv(GL_LIGHT0, GL_SPECULAR, specularLight);
    
    glLightfv(GL_LIGHT1, GL_AMBIENT, new_ambient);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, diffuseLight);
    glLightfv(GL_LIGHT1, GL_SPECULAR, specularLight);
}

void disableLight(){
    glDisable(GL_COLOR_MATERIAL);
    glDisable(GL_LIGHTING);
    glDisable(GL_LIGHT0);
    glDisable(GL_LIGHT1);
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);

    std::cout << "1                   : Quay nguoc chieu kim dong ho" << std::endl;
    std::cout << "2                   : Quay cung chieu kim dong ho" << std::endl;
    std::cout << "3                   : Bat tat che do to mau nang cao" << std::endl;
    std::cout << "v, V                : Chuyen doi giua 2 che do nhin" << std::endl;
    std::cout << "w, W                : Chuyen doi giua che do khung day va to mau" << std::endl;
    std::cout << "+                   : Tang/Giam khoang cach camera" << std::endl;
    std::cout << "-                   : Giam khoang cach camera" << std::endl;
    std::cout << "up arrow/down arrow : Tang chieu cao camera" << std::endl;
    std::cout << "down arrow          : Giam chieu cao camera" << std::endl;
    std::cout << "<-                  : Quay nguoc chieu kim dong ho" << std::endl;
    std::cout << "->                  : Quay cung chieu kim dong ho" << std::endl;

//    glEnable(GL_DEPTH_TEST);

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(SCREEN_WIDTH*2, SCREEN_HEIGHT);
    glutInitWindowPosition(100, 100);

    glutCreateWindow("NguyenVanBaoNguyen - 2013930");

    glClearColor(1.0, 1.0, 1.0, 1.0);
    // glutDisplayFunc(display);
    // glutKeyboardFunc(toggleFillMode);
    // glutSpecialFunc(specialKey);
//    glutTimerFunc(50, update, 0);
    glEnable(GL_DEPTH_TEST);
    glutMainLoop();
    return 0;
}