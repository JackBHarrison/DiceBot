import discord
import random
import re

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

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
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

        while y < 6:
            while i < 4:
                rand = random.randint(1,6)
                arr.append(rand)
                i+=1
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
        txt = message.content[1:]
        if txt[0] == "d" or txt[0] == "D":
            txt = '1'+txt
        x = re.split("d|D", txt)
        i=0
        sum = 0
        while i < int(x[0]):
            rand = random.randint(1,int(x[1]))
            dice.append(rand)
            sum += rand
            i+=1
        roll = ', '.join(str(x) for x in dice)
        total = "Total is: "+str(sum)
        roll = "["+roll+"]"
        await message.channel.send(total)
        await message.channel.send(roll)



