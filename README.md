# COMP3522_Assignment2 
<p>Leon Lee A01062166 </p>
<p>John Han A01064824 </p>
<p> 2020/03/25 </p>
<p> Set: 3T </p>


# The Souvenuir Store 
<p> This application simulates a sovenuir store system that is used by employees to manage inventory orders and transactions. The user can process web-orders, manage inventory, and generate daily transaction report based on orders. <p/>


## User Menu
- Process Web Orders <br>
Proccesses a file (.xlsx) containing a list of web orders. When an item's inventory is sufficient, the item inventory quantity is updated accordingly if a successful transaction is made. Unsuccessful transactions, as a rersult of misinformation in the item order property, will be skipped. Also, the item is made restocked when the inventory is insufficient or out of stock. 
- Check Inventory <br>
Displays the store's current inventory stock of all items.
- Exit <br>
Exits the program. A transaction report containing all orders processed is generated.

## Classes
- UserMenu <br>
Executes the program by providing performable choices
- OrderProcessor <br>
Contains logic for processing file orders 
- Order <br>
Contains information about an item order
- Store <br>
Contains store information
- SeasonalItemFactory <br>
Contains infromation about an item factory
- ChristmasItemFactory <br>
A type of SeasonalItemFactory
- HalloweenItemFactory <br>
A type of SeasonalItemFactory
- EasterItemFactory <br>
A type of SeasonalItemFactory
- FactoryEnum <br>
An Enum of item types producable by an SeasonalItemFactory 
- Item <br>
Contains item information
- Toy <br>
A type of Item
- SantaWorkshop <br>
A type of Toy
- RCSpider <br>
A type of Toy
- RobotBunny <br>
A type of Toy
- StuffedAnimal <br>
A type of Item
- DancingSkeletons <br>
A type of StuffedAnimal
- Reindeer <br>
A type of StuffedAnimal
- EasterBunny <br>
A type of StuffedAnimal
- Candy <br>
A type of Item
- PumpkinCaramelToffee <br>
A type of Candy
- CandyCane <br>
A type of Candy
- CremeEggs <br>
A type of Candy
- InvalidDataError <br>
A type of Exception 


## Diagrams
<ul> UML Class Diagram link: https://www.lucidchart.com/invitations/accept/82806647-624b-4402-9781-6f18fac06432 </ul>
<ul> UML Sequence Diagram link: https://www.lucidchart.com/documents/edit/c4555659-d80b-4497-874d-c74e84652854/0_0 </ul>

