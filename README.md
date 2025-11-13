# WGUPS Routing Program

**Course:** WGU C950 – Data Structures and Algorithms II  
**Project Type:** Python Project  

---

## Project Overview
This project simulates a package delivery system for a delivery company, optimizing routes for multiple packages.  
It demonstrates problem-solving, data structure implementation, and algorithm design while handling a realistic delivery scenario.

---

## Skills Demonstrated
- Designing and implementing algorithms for route optimization (Nearest Neighbor Algorithm)  
- Efficient package management using hash tables  
- File input/output handling  
- Organizing and mapping packages to delivery routes  
- Debugging and testing Python programs for correctness and efficiency  

---

## My Contributions
- Implemented the **Nearest Neighbor Algorithm** to determine optimal delivery routes for 27 unique addresses and 40 packages.  
- Mapped packages to the calculated route stops and created a delivery plan.  
- Tested and debugged the system to ensure correct delivery times and package assignments.  
- Documented code and organized project structure for clarity and maintainability.  

---

## Scenario
This task is the implementation phase of the WGUPS Routing Program.

The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution for their daily local deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements that are listed in the attached “WGUPS Package File.”

Your task is to determine an algorithm, write code, and present a solution where all 40 packages will be delivered on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for all trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map,” and distances to each location are given in the attached “WGUPS Distance Table.” The intent is to use the program for this specific location and also for many other cities in each state where WGU has a presence. Include detailed comments to make your code easy to follow and justify the decisions made.

The supervisor should be able to see, at assigned points, the progress of each truck and its packages, including what has been delivered and at what time.

---

## Assumptions
- Each truck can carry a maximum of 16 packages; package IDs are unique.  
- Trucks travel at an average speed of 18 miles per hour with infinite fuel.  
- No collisions occur.  
- Three trucks and two drivers are available. Drivers stay with the same truck.  
- Drivers leave the hub no earlier than 8:00 a.m., fully loaded, and can return for additional packages if needed.  
- Delivery and loading times are instantaneous.  
- Each package has up to one special note.  
- The delivery address for package #9 is incorrect and corrected at 10:20 a.m.  
- Distances are equal regardless of travel direction.  
- The day ends when all 40 packages are delivered.

---

## Requirements
- Submission must represent original work; adherence to WGU Academic Authenticity rules is required.  
- Professional Communication is assessed automatically through Grammarly for Education.  
- Supporting documentation (screenshots, outputs) should be submitted as PDF files.  
- Only built-in data structures are allowed, except dictionaries.

### Task Breakdown
**A. Hash Table**  
- Develop a hash table with an insertion function that stores the following for each package:
  - Delivery address  
  - Delivery deadline  
  - Delivery city  
  - Zip code  
  - Package weight  
  - Delivery status (at hub, en route, delivered) including delivery time  

**B. Lookup Function**  
- Create a lookup function returning all fields above by package ID.  

**C. Program Implementation**  
- Deliver all packages according to the scenario using the supplied files.  
- Include identifying comment with student ID in `main.py`.  
- Add detailed comments explaining process and flow.  

**D. User Interface**  
- Provide intuitive interface to view delivery status and total mileage.  
- Include screenshots at specific times:
  - 8:35 a.m. – 9:25 a.m.  
  - 9:35 a.m. – 10:25 a.m.  
  - 12:03 p.m. – 1:12 p.m.  

**E. Completion Screenshots**  
- Include screenshots showing successful delivery completion with total mileage.

**F. Algorithm Justification**  
- Describe two or more strengths of the implemented algorithm.  
- Verify algorithm meets all scenario requirements.  
- Identify two alternative algorithms and explain differences.  

**G. Reflection**  
- Describe what you would do differently if repeating the project, including modifications.

**H. Data Structure Verification**  
- Verify the hash table meets all scenario requirements.  
- Identify two alternative data structures and explain differences.

---