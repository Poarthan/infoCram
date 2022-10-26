#!/usr/bin/env python3

import time
import random

def main():
 speed=1
 klevel=0
 try:
  speed=int(input("What speed do you want to learn? (0) Slow (1) Fast:"))
 except ValueError:
  print("bad input, default speed is slow")
 try:
  klevel=int(input("How much do you know about this study set? (0) almost none (1) some (2) almost all (3) test me:"))
 except ValueError:
  print("bad input, default knowledge is 0")
 if klevel >= 3:
  print("testing")
  full_test(tolearn)
 else:
  slist="studylist.mem"
  matchsplchar="!!!!!"
  tolearn, progress_list=matchinglist(slist, matchsplchar, klevel)
  result=learn(tolearn, speed, klevel)
  klevelcal=knowledgecalc(result)

def learn(learnlist, speed, klevel):
 print("oof", speed)
 if klevel > 2.9:
  setquestion=4
  setcoef=1
 elif klevel > 1.9:
  setquestion=2
  setcoef=1
 elif klevel > 0:
  setquestion=3
  setcoef=2
 elif klevel==0:
  setquestion=0
  setcoef=7
 success, question_num=question1mcq(learnlist, learnlist, True)
 success, question_num, difficulty=question2write(learnlist, True)
 rounds=1
 learnlist,otherstore=listconfig(success, question_num, qtype)
 knowledgecalc(result, rounds, speed, klevel)

def listconfig(success, question_num, qtype, matchsplitchar, testlist):
 if success==True:
  if qtype==3:
   level=3
  elif qtype==2:
   level=3
  elif qtype==1:
   level=1
  elif qtype==0:
   level=1
 else:
  if qtype==3:
   level=-1
  elif qtype==2:
   level=-1
  elif qtype==1:
   level=-3
  elif qtype==0:
   level=-3
 prev_quests=testlist[question_num][2].append(qtype)
 knowledgescore=testlist[question_num][3]+level
 
def knowledgecalc(result, rounds, speed, klevel):
 print(result, rounds, speed, klevel)

def question1mcq(testlist, matchlist, withrandom):
 y=len(testlist)
 rand_q=random.randint(0,y-1)
 question=testlist[rand_q][0]
 rand_a=random.randint(0,3)
 random_answer1=rand_q
 rand_ans=testlist[rand_q][1]
 random_answer1=rand_ans
 while random_answer1==rand_ans:
  random_answer1=matchlist[ random.randint(0,len(matchlist)-1)][1]
 random_answer2=rand_ans
 while random_answer2==rand_ans or random_answer2==random_answer1:
  random_answer2=matchlist[random.randint(0,len(matchlist)-1)][1]
 random_answer3=rand_ans
 while random_answer3==rand_ans or random_answer3==random_answer1 or random_answer3==random_answer2:
  random_answer3=matchlist[random.randint(0,len(matchlist)-1)][1]
 print(question)
 # random_answer1=matchlist(random_answer1[1])
 # random_answer2=matchlist(random_answer2[1])
 # random_answer2=matchlist(random_answer3[1])
 if rand_a==0:
  print("(a)", rand_ans)
  print("(b)", random_answer1)
  print("(c)", random_answer2)
  print("(d)", random_answer3)
 elif rand_a==1:
  print("(a)", random_answer1)
  print("(b)", rand_ans)
  print("(c)", random_answer2)
  print("(d)", random_answer3)
 elif rand_a==2:
  print("(a)", random_answer1)
  print("(b)", random_answer2)
  print("(c)", rand_ans)
  print("(d)", random_answer3)
 elif rand_a==3:
  print("(a)", random_answer1)
  print("(b)", random_answer2)
  print("(c)", random_answer3)
  print("(d)", rand_ans)
 user_answer=input("Answer:")
 print("Your answer:", user_answer)
 if user_answer=="a":
  user_answer=0
 if user_answer=="b":
  user_answer=1
 if user_answer=="c":
  user_answer=2
 if user_answer=="d":
  user_answer=3
 if user_answer==rand_a:
  print("Correct!")
  print(rand_ans)
  return True, rand_q
 else:
  print("INCORRECT  :(")
  print(rand_ans)
  return False, rand_q

def question2write(testlist, withrandom):
 y=len(testlist)
 rand_q=random.randint(0,y-1)
 question=testlist[rand_q][0]
 rand_ans=testlist[rand_q][1]
 print(question)
 user_answer=input("Answer:")
 print("Your answer:", user_answer)
 if user_answer==rand_ans:
  print("Correct!")
  print(rand_ans)
  user_level=input("How hard was that to recall, (1, easy-5, very hard), or actually I was INCORRECT(n):")
  if user_level.isdigit():
   user_level=int(user_level)
   if user_level>0 and user_level<=5:
    return True, rand_q, user_level
   else:
    return True, rand_q, 5
  elif isinstance(user_level, str):
   if user_level=="n":
    print("INCORRECT ")
    return False, rand_q, 0
  else:
   return True, rand_q, 5
 else:
  print("INCORRECT ")
  print(rand_ans)
  user_level=input("Overide I was correct, rate how easy it was to recall(1, easy-5, very hard), else just enter:")
  if user_level.isdigit():
   user_level=int(user_level)
   if user_level>0 and user_level<=5:
    print("Correct!")
    return True, rand_q, user_level
   else:
    return False, rand_q, 0
  else:
   return False, rand_q , 0
   
def question3NOTNOW(knowlist, testlist, matchlist, withrandom):
 x=len(testlist)
 y=len(unknownlist)
 rand_q=random.randint(0,y-1)
 question=unknownlist(rand_q[0])
 rand_a=random.randint(0,3)
 random_answer1=rand_q
 while random_answer1==rand_q:
  rand_answer1=random.randint(0,x+y-2)
 while random_answer2==rand_q or random_answer2==random_answer1:
  rand_answer2=random.randint(0,x+y-2)
 while random_answer3==rand_q or random_answer3==random_answer1 or random_answer3==random_answer2:
  rand_answer3=random.randint(0,x+y-2)
 print(question)
 rand_a=unknownlist(rand_q)
 random_answer1=matchlist(random_answer1[1])
 random_answer2=matchlist(random_answer2[1])
 random_answer2=matchlist(random_answer3[1])
 if rand_a==0:
  print("(a)", rand_a)
  print("(b)", random_answer1)
  print("(c)", random_answer2)
  print("(d)", random_answer3)
 elif rand_a==1:
  print("(a)", random_answer1)
  print("(b)", rand_a)
  print("(c)", random_answer2)
  print("(d)", random_answer3)
 elif rand_a==2:
  print("(a)", random_answer1)
  print("(b)", rand_a)
  print("(c)", random_answer2)
  print("(d)", random_answer3)
 elif rand_a==3:
  print("(a)", random_answer1)
  print("(b)", rand_a)
  print("(c)", random_answer2)
  print("(d)", random_answer3)
 user_answer=input("Answer:")
 if user_answer=="a":
  user_answer=1
 if user_answer=="b":
  user_answer=2
 if user_answer=="c":
  user_answer=3
 if user_answer=="d":
  user_answer=4
 if user_answer==rand_a:
  print("Correct!")
  return True, rand_q
 else:
  print("__INCORRECT__  :(")
  return False, rand_q

def question(qtype):
 if qtype==0:
  print(tolearn[random.randint(len(tolearn))])
  input=int(print("?"))
 elif qtype==1:
  print("test1")
 elif qtype==2:
  print("test2")
 elif qtype==3:
  print("test3")
  
def knowledgecalc(results):
 print("knowledge level calaculation")

def matchinglist(slist, matchsplitchar, defaultlevel):
 newlines=[]
 with open(f'{slist}') as file:
  lines = [line.rstrip() for line in file]

 for stuff in lines:
  things=stuff.split(matchsplitchar)
  newlines.append(things)
 progresslist=newlines
 for i in range(len(progresslist)):
  progresslist[i].append([])
  progresslist[i].append(defaultlevel)
 #print(newlines)
 #print(progresslist)
 return newlines, progresslist

def full_test(testlist):
 question_list=testlist
 tested=[]
 correct_incorrect=[]
 correct=0
 for i in range(len(testlist)):
  test_q=random.randint(0, len(testlist)-1)
  print(testlist[test_q][0])
  #print(testlist[test_q[0]])
  user_input=input("Answer:")
  if user_input==testlist[test_q][1]:
   print("Correct")
   print(testlist[test_q][1])
   correction=input("overide I was incorrect?")
   if correction == "Y" or correction == "y":
    print("Incorrect")
    correct_incorrect.append("0")
   else:
    correct_incorrect.append("1")
    correct+=1
  else:
   print("Incorrect")
   print(testlist[test_q][1])
   correction=input("overide I was correct?")
   if correction == "Y" or correction == "y":
    print("Correct")
    correct_incorrect.append("1")
    correct+=1
   else:
    correct_incorrect.append("0")
  tested.append(testlist[test_q])
  testlist.pop(test_q)
 print("You got", correct, "correct out of ", len(question_list))
 print("wrong question check coming soon...., end test anytime stuff coming soon, and replaces test questions thing coming soon")

if __name__ == "__main__":
 main()
