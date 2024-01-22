//## C++ Code ####################################
typedef struct _node
{
    int _data;
    struct _node* _next;
}Node;

class MyList
{
    Node* _head;

public:
    MyList()
    {
        _head = NULL;
    }

    bool Append(int data)
    {
        //Create a new Node
        //Traverse the existing list to the end
        //Place the new node at the last location
        return true;
    }

    int GetAt(int idx)
    {
        Node* temp = _head;

        while (idx > 0)
        {
            temp = temp->_next;
            idx--;
        }

        return temp->_data;
    }

    int operator[](int idx)
    {
        Node* temp = _head;

        while (idx > 0)
        {
            temp = temp->_next;
            idx--;
        }

        return temp->_data;
    }

    void Print()
    {
        // Step through each node and print the data in it.
    }
};


// Consumer
int main()
{
    MyList lst1 = MyList();
    lst1.Append(10);
    lst1.Append(10);
    lst1.Append(10);
    lst1.Append(1000); //4th node data 
    lst1.Append(10);
    lst1.Append(10);
    lst1.Append(10);
    lst1.Append(10);
    lst1.Append(10);
    lst1.Append(10);
    

    cout << lst1.GetAt(4) << endl;

    cout << lst1[4] << endl;
}