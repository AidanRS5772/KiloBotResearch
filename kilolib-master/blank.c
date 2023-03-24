#include "kilolib.h"
#define DEBUG

void setup() { }
int i = 1;
void loop() {
    i++;
    spinup_motors();
    set_motors(kilo_straight_left, kilo_straight_right);
    if(i%2 == 0){
        set_color(RGB(0,1,0));
    }
    else{
        set_color(RGB(0,0,1));
    }

    delay(60000);

}
int main() {
    kilo_init();
    kilo_start(setup, loop);
    return 0;
}
