# Threading-VS-Multiprocessing

A collection of python scripts that use Threading and Multiprocessing

## Programs:
### Prime number finder
#### Discription and Findings
> This group of scripts attempts to show the use cases of theading and multiprocessing by finding prime numbers using thread and process pools. 
___
<s>However the timed results show that neither method improved the time to complete in my testing. My thought was that the threading would be the slowest of the three tests as the function was CPU dependent not I/O dependent. For some reason the slowest was the multiprocessing might just be my PC or I need to rework my code.</s> <br>The issue was the ProcessPoolExecutor, changed to using the Pool function from the multiprocessing method now the test results look more like what I thought it should
___
#### TODO
> - Add args for easier testing
> - <s>Learn why I'm getting unexpected results and adapt the tests</s> DONE!
> - <s>Clean up imports</s> DONE!
> - Attempt to combine mutiprocessing and threading 
### Webspider that uses Threading and Multiprocessing
#### TODO
> - Come up with a good name
> - Write the program
> - Create logic that swaps between the requests and Selenium Modules dependent on 200 codes
