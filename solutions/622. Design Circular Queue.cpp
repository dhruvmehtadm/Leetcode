class MyCircularQueue {
private:
    queue<int> queue;
    int maxsize;
public:
    MyCircularQueue(int k) : maxsize(k) {
        
    }
    
    bool enQueue(int value) {
        if(queue.size()==maxsize){
            return false;
        }
        else{
            queue.push(value);
            return true;
        }
    }
    
    bool deQueue() {
        if(queue.size()==0){
            return false;
        }
        else{
            queue.pop();
            return true;
        }
    }
    
    int Front() {
        if(queue.size()==0){
            return -1;
        }
        else{
            return queue.front();
        }
    }
    
    int Rear() {
        if(queue.size()==0){
            return -1;
