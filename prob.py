def probability(sample_space,event):
    n_of_event=0
    for i in sample_space:
        if i==event:
            n_of_event=1
            probability=n_of_event/len(sample_space)
            return probability
sample_space=["head","tail"]
event="head"
print(probability(sample_space,event))

