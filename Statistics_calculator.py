import numpy as np
dataset = []
b = int(input("Enter how many data values you want to input:- "))
for i in range(b):
    value = float(input("Enter the Data:- "))
    dataset.append(value )
print(dataset)
while True:
    arr = np.array(dataset)
    choice = input("1. Mean\n2. Variance\n3. Median\n"
              "4. Standard Deviation(std)\n5. Max\n6. Min"
              "\n7. Sum\n8. Percentile\n9. Exit\nEnter Your Choice:- ")
    if choice == "mean" or choice == "1":
        mean = np.mean(arr)
        print("Mean:-",mean)
    elif  choice == "variance" or choice == "2":
        variance = np.var(arr)
        print("Variance:-",variance)
    elif choice == "median" or choice == "3":
        median = np.median(arr)
        print("Median:-",median)
    elif choice == "std" or choice == "4":
        std = np.std(arr)
        print("Standard Deviation:-",std)
    elif choice == "max" or choice == "5":
        maximum = np.max(arr)
        print("Maximum:-",maximum)
    elif choice == "min" or choice == "6":
        minimum = np.min(arr)
        print("Minimum:-",minimum)
    elif choice == "sum" or choice == "7":
        add = np.sum(arr)
        print("Sum:-",add)
    elif choice == "percentile" or choice == "8":
        p = float(input("Enter percentile (0-100):- "))
        percentile = np.percentile(arr,p)
        print("Percentile:-",percentile)
    elif choice == 'exit' or choice == "9":
        print("Thank You")
        break
    else:
        print("Invalid choice")
