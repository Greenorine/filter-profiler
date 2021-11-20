# filter-profiler  
filter.py  
![pycharm64_r5TVO8IxqD](https://user-images.githubusercontent.com/41028671/142731490-45a46fa1-d481-409b-a96d-23c44fe783c0.png)  

old_filter.py  
![image](https://user-images.githubusercontent.com/41028671/142731556-541e4fa3-e6f8-4f96-b8f1-0c8a1092d6d2.png)  

Результаты разные, поскольку в filter.py ожидается ввод, нужно некоторое время, чтобы ввести все данные, оно числится в профайлере  

![image](https://user-images.githubusercontent.com/41028671/142731842-6577f516-4d73-4d40-8e14-ec73f998af89.png)  
Время выполнения примерно одинаковое применимо к случаю old_filter.py, но вызовов функций было больше, это вызвано тем, что функций в целом стало больше, а также расширены границы, т.к. old_filter содержал ошибки в виде неправильных границ, что создавало меньшее итерируемое поле значений.
