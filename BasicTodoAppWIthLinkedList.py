


class Node:
    counter = 0; #class varaible
    def __init__(self , task):
        self.task = task;
        Node.counter = Node.counter + 1;
        self.taskId = Node.counter;
        self.next = None;
        '''
        Ecah node is a data object! 
        {
            "task": "Go to gym",
            "next": none; this next is the memory location of another object somewhre in the memory! for now it is none;

        }


            todo = ToDoList()

            # create nodes (tasks)
            n1 = Node("Go to gym")
            n2 = Node("Do DSA problem")

            # link them
            n1.next = n2

            # put the first node into the ToDoList
            todo.head = n1

        '''
class toDo():
    def __init__(self):
        self.head = None;

    def addTask(self, task):
        newNode = Node(task);
        if not self.head:
            self.head = newNode;
        else:
            current = self.head;
            while current.next:
                current = current.next;
            current.next = newNode;
        

    def showTasks(self ):
        print("--------------Your Tasks------------------");
        tasks = [];
        if not self.head:
            return "The TodoList is empty";
        else:
            current = self.head;
            while current:
                tasks.append(current.task);
                current = current.next;
            return tasks;

        
        

    def deleteTask(self , Id):
        # logic to delete head node
        current = self.head;
        prev = None;
        if self.head.taskId == Id:
            self.head = current.next;
        # logic to delete any node
        while current:
            if current.taskId == Id:
                prev.next = current.next;
                return "Node Deleted Successfully";
            else:
                prev = current;
                current = current.next;
        #logic to delete last node;
        
            



def main():
    # hellot
    # task = Node("Pray Namaz And thank Allah");
    # task1 = Node("go to gym");
    # task2 = Node("Solve dsa problem");

    # task.next = task1;
    # task1.next = task2;


    todo = toDo();
    todo.addTask("Pray Namaz And thank Allah");
    todo.addTask("go to gym");
    todo.addTask("solve a dsa problem");
    output = todo.showTasks();
    print(output);
    message = todo.deleteTask(2);
    print(message);
    output1 = todo.showTasks();
    print(output1);
    
    print(todo.deleteTask(3));
    print(todo.showTasks());


    '''
    ToDoList
        head
        |
        v
    +-------------------+      +-------------------+      +-------------------+
    | task: Pray Namaz  | ---> | task: Go to gym   | ---> | task: DSA problem |
    | next: points next |      | next: points next |      | next: None        |
    +-------------------+      +-------------------+      +-------------------+



    '''


if __name__ == "__main__":
    main();
