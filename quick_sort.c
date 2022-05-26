void _quickSortPointer(int *begin, int *end) { 
    if (begin >= end)
        return;

    int pivo = *(begin + ((end - begin) >> 1));
    int *l = begin;
    int *r = end;
    
    do{ 
        while(*l < pivo && l <= r)
            l++;
        while(*r > pivo && r >= l)
            r--;
            
        if(l <= r){
            swap(r, l);
            l++;
            r--;
        }

    } while(l < r);
    
    _quickSortPointer(begin, r);
    _quickSortPointer(l, end);
}

void quickSortPointer(int *vet, int size){
    _quickSortPointer(vet, vet + size - 1);
}
