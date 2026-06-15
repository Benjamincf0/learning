#define PPM_PIN 3
#define NUM_CHANNELS 4
#define PULSE_WIDTH 300      // fixed high pulse in µs between each channel
#define START_FRAME 2100     // This basically separates frames (> 2ms as per wikipedia)
#define FRAME_LENGTH 20000   // total frame length in µs (20ms)

// In RC the channel values typically range between 1000 and 2000, therefore 15000 is a neutral midpoint.
// Except for throttle which should start at 1000 since it's off.
// Channels: Aileron=Roll, Elevator = Pitch, Throttle, Rudder = yaw
int channels[NUM_CHANNELS] = {1500, 1500, 1000, 1500};

// The Radiomaster boxer runs the open-sourced Edge-TX software. EdgeTX has a Trainer/Student mode which allows a Slave controller to be connected to a Master and send it RC controls that it then sends to the drone via ELRS.
// The Slave controller sends controls via a combined pulse-position modulated (CPPM) signal, which allows multiple channels to be sent accross the same cable as described in this article:
// https://en.wikipedia.org/wiki/Pulse-position_modulation#:~:text=edit%5D-,A,tags%2E
// A stream of packets through the ppm signal would something like this
// HIGH(start >2ms) | LOW(0.3ms) HIGH(ch1) | LOW(0.3ms) HIGH(ch2) | ... | LOW(0.3ms) HIGH(chN) | [frame padding]
void sendPPMFrame() {
    unsigned long frameStart = micros();
    
    // start frame 
    digitalWrite(PPM_PIN, HIGH);
    delayMicroseconds(START_FRAME);

    for (int i = 0; i < NUM_CHANNELS; i++) {
        // Serial.print(channels[i]);
        // Serial.print(" ");

        // LOW pulse
        digitalWrite(PPM_PIN, LOW);
        delayMicroseconds(PULSE_WIDTH);

        // HIGH pulse
        // Since each channel (up to 8) is encoded by the time of the high state plus the lower state. (PPM high state + 0.3 = servo PWM pulse width), we subtract the pulse width from the target channel value.
        // As such, we can't set a channel to less than START_FRAME.
        digitalWrite(PPM_PIN, HIGH);
        delayMicroseconds(max(channels[i] - PULSE_WIDTH, 0));
    }
    // Serial.println();
    digitalWrite(PPM_PIN, LOW);

    // Wait out the rest of the frame, so that the receiver can receive them at a regular interval.
    unsigned long elapsed = micros() - frameStart;
    if (elapsed < FRAME_LENGTH) {
        delayMicroseconds(FRAME_LENGTH - elapsed);
    }
}

void setup() {
    Serial.begin(115200);
    pinMode(PPM_PIN, OUTPUT);
    digitalWrite(PPM_PIN, LOW);
}

void loop() {
    // example: sweep channel 1 (throttle) up and down
    for (int val = 1000; val <= 2000; val += 10) {
        channels[2] = val;
        sendPPMFrame();
    }
    for (int val = 2000; val >= 1000; val -= 10) {
        channels[2] = val;
        sendPPMFrame();
    }
}
