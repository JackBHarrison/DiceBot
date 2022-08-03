import discord
import re
import random

def mergeSort(arr):
    if len(arr) > 1:
 
        # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        left = arr[:mid]
        right = arr[mid:]
 
        # Sorting the first half
        mergeSort(left)
 
        # Sorting the second half
        mergeSort(right)
 
        i = j = k = 0
 
        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

#starts client
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#checks that the bot is not respondind to its own message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #rolls 4d6 drop 1
    if message.content.startswith('$character'):
        dice = []
        i=0
        y=0
        roll = ''
        att = ''
        arr = []
        sum = 0
        stat = 0
        stats = []

        #rolls 4 dice six times
        while y < 6:
            while i < 4:
                rand = random.randint(1,6)
                arr.append(rand)
                i+=1
            #sorts and does not count lowest number    
            mergeSort(arr)
            i = 0
            while i < 3:
                stat += arr[i]
                i+= 1
            sum += stat
            stats.append(stat)
            stat=0
            i=0
            dice.append(arr)
            arr = []
            y+=1
        #formats the dice rolls
        for x in dice:
            roll = roll+"["
            roll += ', '.join(str(y) for y in x)
            roll = roll+"]  "
        i = 0
        att += ', '.join(str(y) for y in stats)
        await message.channel.send(att)
        await message.channel.send(roll)
        total = "Total: "+str(sum)
        await message.channel.send(total)
        return

    if message.content.startswith('$'):
        dice = []
        op = 0
        #changes op depending on if the message contains a + or minus operator
        if "+" in message.content:
            op = 1
        if "-" in message.content:
            op = 2
        #removes $
        txt = message.content[1:]
        #makes the number of rolls one if left blank
        if txt[0] == "d" or txt[0] == "D":
            txt = '1'+txt
        x = re.split("d|D|\+|\-", txt)
        i=0
        sum = 0
        while i < int(x[0]):
            rand = random.randint(1,int(x[1]))
            dice.append(rand)
            sum += rand
            i+=1
        roll = ', '.join(str(x) for x in dice)
        if op == 1:
            sum += int(x[2])
        if op == 2:
            sum -= int(x[2])
        total = "Total is: "+str(sum)
        roll = "["+roll+"]"
        await message.channel.send(total)
        await message.channel.send(roll)

f = open("token.txt", "r")
token=f.readline()
client.run(token)

