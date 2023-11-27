# Smart-Theater-Using-Raspberry-Pi-Pico (BASA Theater)

# 1.0	Introduction
## 1.1 Purpose of the Report
This report shows a system developed to create a wholly automated 4-sided room and any shop to make it a fully automated room that saves electricity and assists humans in managing the number of people in the room septically when an epidemic occurs in a city and social-distance required.
## 1.2 Background of the Report 

The idea is inspired by the precautionary actions to novel coronavirus spread over the globe and social-distance were required in malls, shops, and most of the facilities in a city with a safe and human-friendly system.
And one of the most significant barriers is the cast of the systems that assist in monitoring a room's electricity consumption - with a pandemic presence or not -and counting people inside the room, on top of that, permitting a specified number of people to be in before reaching the limit and vice versa.
## 1.3 Scope of the Report 

The report provides a tested model system of a theater called BASA theater using Raspberry Pi Pico microcontroller board, programmed with MicroPython programming language.
	We built an integrated system that has two modes, default mode, where the system opens doors/gates, monitors people's presence and electrical supply in the room automatically, with the aid of cheap component (10$ - 15$) Buzzer, Raspberry Pi Pico microcontroller, LEDs (representing electrical devices in the room),  LCD screen, Infrared Receiver with remote control, 2 servo motors and 2 ultrasonic sensors. 
Note: A basic understanding of electronics and electrical circuit terminology is assumed.

# 2.0	Objectives and Problem Statement 
During the novel pandemic long period, mall, shops and most commercial facilities were risked of continuing work with more strict regulations; therefore, there were a need to employ a system or an employee to count people number in the room in order to keep people's number under the limit which is not practical during emergencies and available with unreasonable price; consequently, there is a need for an affordable system that communicates with customers actively via screen -as an example- and alerts with the room's capacity is exceeded or reached.

	The objectives of our project are as follows:
1.	Establishing a practical system that can replace a watcher's job with all functions of counting and alerting.
2.	Finding an affordable alternative that can be produced in a short time at a reasonable price.
3.	Finding a safe alternative that considers emergency considerations and presents a solution when there is a malfunction in the system or when there is an unexpected demand.
4.	Utilizing proper methods of alerting, conveying a message, and fully automated.

# 3.0	Topic
## 3.1	Methodology
![image](https://github.com/Ammarhmm6/Smart-Theater-Using-Raspberry-Pi-Pico/assets/152064504/fac73031-f57f-4a73-9b6c-caa477b78b20)

## 3.2	Schematic Diagram

![image](https://github.com/Ammarhmm6/Smart-Theater-Using-Raspberry-Pi-Pico/assets/152064504/6f2dc13f-d056-4be9-b1ba-11c2c60e4d97)

## 3.3	Flow Chart

![image](https://github.com/Ammarhmm6/Smart-Theater-Using-Raspberry-Pi-Pico/assets/152064504/47993514-504d-4d0d-a6cc-e2911166f659)


# 4.0	Result
![image](https://github.com/Ammarhmm6/Smart-Theater-Using-Raspberry-Pi-Pico/assets/152064504/9f648aef-045e-412f-8e8a-302815038cd9)

As shown in Table 1, When a person comes and wants to enter the BASA theater, an Ultrasonic will detect if he can enter or not because the number of people allowed to enter is 5. However, if there is no one inside, the gate will start opening using a Servomotor, it will close after 2.5s, and the LEDs will turn on if there are five inside. The buzzer will start to emit a buzz, and the Lcd with Adapter L2c will be showing (The number of people in the room has reached the limit; therefore, you are not allowed in).
When BASA theater's show is finished, and the audience wants to leave, the Ultrasonic will detect the people approaching the doors to go; the doors will open for them automatically via two servo motors. LEDs will -simultaneously- turn off when the last one leaves through the door. 
We did an emergency mode to make sure of audience safety. If there were 4 of the audience inside and for some reason or emergencies such as fire or spread of flammable gas in the place or the flood of water; at that moment, via the remote control, the system would change to emergency mode, and the ultrasonic sensor will not work. Hence, via the remote control, we can switch on and off the lights and control the doors manually.

# 5.0	 Discussion
 
We achieved the desired objectives and provided security and protection for the audiences considering the Corona pandemic by reducing the number of attendees and arranging their entry for not everyone at the same time. We developed a theater using Raspberry Pi Pico microcontroller board, programmed with MicroPython programming language.
One of the advantages of our project is that it is cheap and adjustable. It can replace any other expensive projects. It can also replace a watcher's job with all functions of counting and alerting. Moreover, it can be beneficial by saving electricity and assisting humans in managing the number of people in the room septically when an epidemic occurs in a city, and social distance is required.
Using a remote control, we could activate the emergency state when it occurred, provide security and protection for the audience, and facilitate their exit from the theatre. We chose this method because it is straightforward, replaces Bluetooth, and may be preferable in the event of an emergency in the theatre.

We also need to restrict who is allowed to enter the theatre. In our project, we utilized the ultrasonic sensor since it is inexpensive and highly effective, replacing many expensive sensors. In other situations and crowded places, we may need to enter them simultaneously to prevent crowding.
At the project's end, we accomplished all the objectives and demonstrated that it was successful and could effectively replace more expensive projects.
# 6.0	Conclusion and Recommendations 

## 6.1	Conclusion
The report has shown a complete view of the reliable cheap embedded system that has emergency mode for any probable malfunction and any unexpected circumstance. 
Raspberry Pi Pico has shown an outstanding capability in respect of its price and size compared with Arduino UNO. Moreover, it is easy to program since it uses MicroPython language with simple-to-understand function detonation.

## 6.2	Recommendations and Future Work
For future work, we recommend increasing the number of proper controlling methods such as smartphone applications and storing people statistics and the number of people in the room in a virtual cloud for securing and inventory purposes.
# 7.0	References

[1] 	 Maier, B. and Brockmann, D., 2020. Effective containment explains subexponential growth in recent confirmed COVID-19 cases in China. Science, 368(6492), pp.742-746.

[2] 	 Bartik, A., Bertrand, M., Cullen, Z., Glaeser, E., Luca, M. and Stanton, C., 2020. The impact of COVID-19 on small business outcomes and expectations. Proceedings of the National Academy of Sciences, 117(30), pp.17656-17666.
