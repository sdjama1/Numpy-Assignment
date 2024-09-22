The purpose of this project is to load data into an ndarray and do data manipulation. I struggled heavily with the first part since i couldnt index the column properly. The first and biggest issue I had
with indexing the array was figuring out how to properly index the data i wanted, such as the field goals made/attempted. Initially using "array[;, :int]" sort of worked but it didnt
isolate the integer i needed for making the accuracy calculations, and i would get a division by zero error, despite using np.where(fga > 0, ....) and I got around that by converting those
values to floats. It wasnt bad after I figured that out, but it sure did cost me some time.



















'''

Explanation of the "def" func:

Name: topplayers
inputs: data, column index, how many top players you want to see
Process: sorts the players based on the stat you want to see, converts data
to floats so calculations can be done, and argsort returns the indices
that would sort the array in ascending order, so [::-1] reverses the order
output: pretty self explanatory
