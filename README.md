# ROSS (Responsive Opposing rockpaperScissors Servant) Bot

This was our submission for Hack Club Scrapyard (March 1-2, 2025). This includes all the code and pictures to create a rock, paper, scissors robot!

## Components

- 3 Soda Cans (We used 2 Coke and a Celsius can for the most optimal build)
- Raspberry Pi Pico 2
- One servo
- Two red LEDs
- One green LED
- Jumper cables
- A bread board
- Three Buttons

## Dependencies

- Adafruit MCP230xx
- Adafruit Motor
- Adafruit Motorkit

## Instructions

1. Clone the repository
2. Flash CircuitPython to your board (guide [here](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython))
3. Install required dependancies (guide [here](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries))
4. Connect your components to the appropriate pins
5. Flash the ROSS Bot to your board
6. ???
7. Profit 
### Microcontroller

For this project, we used a [Raspberry Pi Pico 2](https://www.raspberrypi.com/products/raspberry-pi-pico-2/) flashed with [CircuitPython](https://circuitpython.org/). This may work with [MicroPython](https://micropython.org/), however we failed multiple times while using it before switching to (the arguably inferior) CircuitPython.
### Board layout
- GP5 - Loser LED
- GP11 - Rock button
- GP14 - Paper button
- GP15 - Scissors button
- GP22 - Winner LED
    
You may change the layout by updating it in code.
## Demo

You may check out the demo video [here](https://www.youtube.com/watch?v=yNPIscg1MPI).  Here are some photos of the bot:
  
![ROSS Bot](https://hc-cdn.hel1.your-objectstorage.com/s/v3/b3aeafc727d2a38b5bfdf56f245a30e9d16b96f3_img_4864.jpg)
![ROSS Bot](https://hc-cdn.hel1.your-objectstorage.com/s/v3/0b9cc506c9a9c43086c54dc1526226a092f90b57_img_4863.jpg)
