#include <stdint.h>
#include <stddef.h>

bool FuzzMe(const uint8_t *Data, size_t DataSize) { //vulnerable code
	return DataSize >= 3 &&
		Data[0] == 'F' &&
		Data[1] == 'U' &&
		Data[2] == 'Z' &&
		Data[3] == 'Z';  
}


//fuzz target function
extern "C" int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size) {
	FuzzMe(Data, Size); 
	return 0;
}
