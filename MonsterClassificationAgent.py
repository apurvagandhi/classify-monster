class MonsterClassificationAgent:
    def __init__(self):
        pass
    
    def solve(self, samples, new_monster):
        positive_traits = {
            'size': [], 
            'color': [],
            'covering': [],
            'foot-type': [],
            'leg-count': [], 
            'arm-count': [], 
            'eye-count': [], 
            'horn-count': [],
            'lays-eggs': [], 
            'has-wings': [], 
            'has-gills': [],
            'has-tail': []
        }
        negative_traits = {
            'size': [], 
            'color': [],
            'covering': [],
            'foot-type': [],
            'leg-count': [], 
            'arm-count': [], 
            'eye-count': [], 
            'horn-count': [],
            'lays-eggs': [], 
            'has-wings': [], 
            'has-gills': [],
            'has-tail': []
        }
        for monster in samples:
            for attribute in monster[0]:
                if monster[1] == True:
                    positive_traits[attribute].append(monster[0][attribute])  
                else:
                    negative_traits[attribute].append(monster[0][attribute])  
        
        for attribute in positive_traits:
            positive_traits[attribute] = list(set(positive_traits[attribute]))
        for attribute in negative_traits:
            negative_traits[attribute] = list(set(negative_traits[attribute]))

        is_positive = True
        for attribute in new_monster:
            if is_positive == True and new_monster[attribute] in positive_traits[attribute]:
                is_positive = True
            elif new_monster[attribute] in negative_traits[attribute]:
                is_negative = True
                is_positive = False
        
        if is_positive:
            return True
        if is_negative:
            return False