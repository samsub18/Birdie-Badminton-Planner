'''
Creating 3 types of lists:
1. warmup 
2. basic_drills
3. end_drills

Now Idea is to select 1 drills from each of the list and put all of them to another list called Day1 , Day2 and so on......
And each drill is to be eliminated from the list once its chosen and transferred to another list called:
1. comp_warmup
2. comp_basic_drills
3. comp_end_drills

The drills which are present in the End Drills are to be done every alternate class.
'''



warmup=[
    "Sprinting 2 courts",
    "Sprint, sacche , butt  kick",
    "6 corner random movement",
    "Butt kick and sprint",
    "Jumping and moving forward",
    "Throwing the shuttle and pickup",
    "Throwing the shuttle and pickup",
    "Relay",
    "Rain tap and 6 corners",
    "High knees and sprint",
    "Sacche and jump",
    "Happy feet (Rain Tap and sprint)",
    "Sacche split step and sprint",
    "Bear crawl",
    "5 Rounds around the court",
    "Sacche blow whistle and sprint",
    "Lunge step",
    "Front , side , back and sprint",
    "Shuttle Run Team game",
    "Balance the racket",
    "Agility",
    "Scissor Jump Exercise",
    "Split step exercise",
    "One leg hop",
    "Line touches with running",
    "Line touches with sacche",
    "Skiing",
    "Diagonal court movement 4 corners",
    "Straight court movemet 4 corners",
    "Duck Walk",
    "Carioca",
    "Touching the Floor",
    "Side to side sacche and jump",
    "High knees",
    "Jumping Jacks",
    "Plank",
    "High Plank",
    "Cone side to side",
    "Zig Zag",
    "Dynamic Warmup with music",
    "Cone High knee",
    "Racket Swinging",
    "Group Agility (Down , Jump , Turn , Sprint)",
]


basic_drills=[
    "Ready, Toss stance, Hit (Group and leader)",
    "Backhand to forehand grip change and lift shot (16 shuttles)",
    "Only toss, fast pace (20 shuttles)",
    "Forehand Action and backhand lift (12 shuttles)",
    "Overhead action and forehand lift (12 shutlles)",
    "Hitting with change of grip (Players throwing)",
    "Dribble shots fh and bkhd (20 shuttles)",
    "Parallel Play with Coach (Teaching to keep racket up)",
    "Sacche and hit on forehand front and backhand front (Out by out )",
    "Net shot and Lift rally : Advance",
    "3 split and lift bkhand and forehand (16 shuttles)",
    "Defence action and dribble (16 shuttles)",
    "Scissor Jump practise and hit (20 shuttles fast pace)",
    "Scissor Jump with movement (bkhand dribble to overhead movement) (20 shuttles)",
    "Full court movement in order (overhead, fh lift , forehand back, bkhnd lift , fh def, bk def , fh tap, bkhand tap)(20 shut)",
    "Smash shot (Near the net practise) (20 shuttles)",
    "Defence Practise (16 shuttles , bkhand and forehand)",
    "Shadows (6 corners)",
    "Shuttle picking (6 corners)",
    "6 corner in order (20 shuttles) (Long and short)",
    "4 corner in order (20 shuttles) (Long and short)",
    "2 corners - forehand lift & forehand toss, backhand lift & overhead toss (20 shuttles)",
    "Flat play (2 players in each half court)",
    "Toss with each other (2 players in each half court)",
    "Merry Go round (3 players in each half court)",
    "Overhead Drop shot (Players Throw) (One shuttle)",
    "Forehand Drop shot (Players Throw) (One shuttle)",
    "Service (16 shuttles each, player on other side receives)",
    "Wall Practise",
    "Serve Hit and Catch on the Wall",
    "Forehand toss , forehand tap , Overhead toss, overhead tap (2 vs 1 with coach) (16 shutlles)",
    "Overhead toss and forhand keep",
    "Forehand toss and backhand keep",
    "2 Overhead toss and forehand lift (20 shuttles) , same on other side",
    "Hit toss and push the shuttle in front (12 shuttles front)",
    "Side to side hitting (20 shuttles)",
    "Forehand action , bkhand action and forehand smash",
    "Backhand action, forehand action and overhead smash",
    "Service practise 2 (Split after serve)",
    "Rules of Badminton Game",
    "Full Court game (21 points)",
    "Half court game (11 points)",
    "Doubles Rotation"
]

end_drills=[
    "Balloon Tap",
    "Mirror Chase",
    "Grip Change with Balloon tap",
    "Shuttle Run Team game",
    "Throwing Game",
    "Keep your court free",
    "Agility Ladder(Jump over boxes, Running, Out and in, One leg jump, Side jumps with both legs together)",
    "Throw on target",
    "Tag Game",
    "Mirror chase and throw",
    "Mobility Exercises",
    "Burpees",
    "Calf Touching",
    "Throwing Game with scissor jump",
    "Statues",
    "Skipping Rope",
    "Dice Run Game",
    "Golf Game (Only if Forehand serve is practised thoroghly)",
    "Balance and Throw",
    "Rounder Game",
    "Out by out rallies",
    "Chinese Game",
    "11 points game",
    "Running Race",
    "Balancing shuttles"
]

day_counter=1  

comp_warmup=[] #completed warmup exercises
comp_basic_drills=[] #completed basic drill exercises
comp_end_drills=[] #completed end drill exercises

warmup_duration = 5
basic_drill_duration = 25
basic_second_drill_duration = 20
end_drill_duration= 10 


counter_enddrill=0

first_ele=0

week_counter=1


#---------------------------------------------------------week1----------------------------------------------------------------#


for x in range(0,8):
    if x==0:
        print(f"Schedule for week{week_counter}: ")
    print(" ")
    print(f"Day{day_counter} :")
    print(f"                 {warmup[first_ele]} duration : {warmup_duration} min\n")
    if x==0 or x%2==0: 
        print(f"                 {basic_drills[first_ele]} duration: {basic_drill_duration} min\n")
        print(f"                 {basic_drills[first_ele+1]} duration: {basic_second_drill_duration}\n")
        
    else:
        print(f"                 {basic_drills[first_ele]} duration: {basic_drill_duration} min\n")
        print(f"                 {basic_drills[first_ele+1]} duration: {basic_drill_duration} min\n")
        
    if x==0 or x%2==0:
        print(f"                 {end_drills[counter_enddrill]} duration: {end_drill_duration} min\n")
        comp_end_drills.append(end_drills.pop(counter_enddrill))
        
    comp_warmup.append(warmup.pop(first_ele))
    comp_basic_drills.append(basic_drills.pop(first_ele))
    comp_basic_drills.append(basic_drills.pop(first_ele))
    
    if day_counter==2:
        break;
        
    day_counter+=1
    
#------------------------------------------------------------------------------------------------------------------------------#    
    
    
    
#--------------------------------------------------week2-----------------------------------------------------------------------#
    
week_counter+=1
day_counter=1
print(" ")
print(" ")
print(" ")
print(" ")
for x in range(0,8):
    if x==0:
        print(f"Schedule for week{week_counter}: ")
    print(" ")
    print(f"Day{day_counter} :")
    print(f"                 {warmup[first_ele]} duration : {warmup_duration} min\n")
    if x==0 or x%2==0: 
        print(f"                 {basic_drills[first_ele]} duration: {basic_drill_duration} min\n")
        print(f"                 {basic_drills[first_ele+1]} duration: {basic_second_drill_duration}\n")
    else:
        print(f"                 {basic_drills[first_ele]} duration: {basic_drill_duration} min\n")
        print(f"                 {basic_drills[first_ele+1]} duration: {basic_drill_duration} min\n")
        
    if x==0 or x%2==0:
        print(f"                 {end_drills[counter_enddrill]} duration: {end_drill_duration} min\n")
        comp_end_drills.append(end_drills.pop(counter_enddrill))
        
    comp_warmup.append(warmup.pop(first_ele))
    comp_basic_drills.append(basic_drills.pop(first_ele))
    comp_basic_drills.append(basic_drills.pop(first_ele))
    
    if day_counter==2:
        break;
        
    day_counter+=1
    
#------------------------------------------------------------------------------------------------------------------------------#    
 

    
#--------------------------------------------------week3-----------------------------------------------------------------------#
    
week_counter+=1
day_counter=1
print(" ")
print(" ")
print(" ")
print(" ")
for x in range(0,8):
    if x==0:
        print(f"Schedule for week{week_counter}: ")
    print(" ")
    print(f"Day{day_counter} :")
    print(f"                 {warmup[first_ele]} duration : {warmup_duration} min\n")
    if x==0 or x%2==0: 
        print(f"                 {basic_drills[first_ele]} duration: {basic_drill_duration} min\n")
        print(f"                 {basic_drills[first_ele+1]} duration: {basic_second_drill_duration}\n")
    else:
        print(f"                 {basic_drills[first_ele]} duration: {basic_drill_duration} min\n")
        print(f"                 {basic_drills[first_ele+1]} duration: {basic_drill_duration} min\n")
        
    if x==0 or x%2==0:
        print(f"                 {end_drills[counter_enddrill]} duration: {end_drill_duration} min\n")
        comp_end_drills.append(end_drills.pop(counter_enddrill))
        
    comp_warmup.append(warmup.pop(first_ele))
    comp_basic_drills.append(basic_drills.pop(first_ele))
    comp_basic_drills.append(basic_drills.pop(first_ele))
    
    if day_counter==2:
        break;
        
    day_counter+=1
    
#------------------------------------------------------------------------------------------------------------------------------#    
 
# You can copy and paste the loops if you want to view future weeks schedule
    
