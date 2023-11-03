
# <p align="center">AirBnB Clone : the console</p>
  
This project is the first step in the construction of an AirBnB clone. We start by building the console.
The diagram below shows this part of the project.

![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231103%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231103T092533Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3a15e451bd35b913bb63b80a738f1c445d37d2f8f3896274071eaef1a58802ac)
    


# <p align="left">Console Setup</p>
  
1. Clone this git repository in your terminal
`git clone git@github.com:lucieruin/holbertonschool-AirBnB_clone.git`

2. Now use the command interpreter to open it
    
```
./console
```
The prompt appears on the next line.

```
(hbnb)
```
3. You can now type your commands, such as 

```
(hbnb) create User
```
Whose console response will be:

```
e1ee8d58-9845-401a-bd74-f599210459e0
```


# <p align="left">Commands</p>
  
Now you can use the console commands. With the `help `command, you have access to the various existing commands integrated into the console
Here's a table of the different commands you can use:



| Name commands | How to type it| What it does
| -------- | -------- | -------- |
| EOF    | Exit the console by EOF (ctrl-D)    | -   |
| all   | `all <classname> `  | Prints the string representations of all instances of a given class    |
| create    | `create <classname>`    | Creates a new instance of a given class, prints ID and save it into a JSON file   |
| destroy   | `destroy <class_name> <id> `  | Deletes a class instance based on a given id   |
 | help    | `help <command> `  | Displays available commands or gives info  |
|quit  | `quit`    |  	Quit the console |
|show | `show <class_name> <id>  ` |  	Prints the string representation of a class instance based on a given id |
|update | `update <class name> <id> <attribute name> "<attribute value>" `|  	 	Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pair |


# <p align="left">Example commands with their output</p>
  
 1. Command `help` 

```

(hbnb) help
```
output:

```
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

```

2. Command `create`

```
(hbnb) create User
```
output:

```
97a37f58-f86b-4f1e-8531-4f03f569a1bb
```

3. Command `all`

```
(hbnb) all BaseModel
```
output:

```
[BaseModel] (f15e7309-4b43-4606-98fd-ac6359d0068a) {'id': 'f15e7309-4b43-4606-98fd-ac6359d0068a', 'created_at': datetime.datetime(2023, 11, 2, 16, 26, 8, 276924), 'updated_at': datetime.datetime(2023, 11, 2, 16, 26, 8, 276975)}
[BaseModel] (ab29744a-37cc-4260-b494-cd1a7956b8f8) {'id': 'ab29744a-37cc-4260-b494-cd1a7956b8f8', 'created_at': datetime.datetime(2023, 11, 2, 16, 26, 9, 290001), 'updated_at': datetime.datetime(2023, 11, 2, 16, 26, 9, 290052)}
```


# <p align="left">Classes</p>
  
1. BaseModel
The BaseModel class is the base class for this project and defines all the attributes for the other classes

Public instance attributes: `id`, `created_at` and `updated_at`

Public instance methods: `save`, `to_dict`


# <p align="left">Other classes(inherits from BaseModel</p>
  

1.User

Public class attributes : `email`, `password`, `first_name` and `last_name`

2.State

Public class attributes : `name`

3.City

Public class attributes: `state_id`, `name`

4.Amenity

Public class attributes: `name`

5.Place
Public class attributes: `city_id`, `user_id,` `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, `amenity_ids`

6.Review

Public class attributes: `place_id`, `user_id`, `text`



# <p align="left">Storage</p>
  
The `FileStorage` class is used to save and load data from a JSON file.

Public instance methods: `all`, `new`, `save`, `reload`


Private class attributes:  `file_path`, `objects`



# <p align="left">Test</p>
  

The use of unittest is shown here. To test all of these you can use the command:

```
python3 -m unittest discover tests
```

whose output should be:

```
...................
----------------------------------------------------------------------
Ran 19 tests in 0.007s

OK
```


# <p align="left">Team</p>
  
- Tartar Mickael:  [https://github.com/mickaeltartar](https://github.com/mickaeltartar)
- Ruin Lucie: [https://github.com/lucieruin](https://github.com/lucieruin)



# <p align="left">License</p>
  
This project is licensed under the MIT License - see the LICENSE file for details.
