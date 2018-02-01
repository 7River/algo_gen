import random
debug=True
class Node(object):
    def __init__(self,name):
        self.name = name
        self.listNodes={}
    def __str__(self):
        return self.name


    def addNode(self,node,cost):
        self.listNodes[node.name]=(node,cost)
        node.listNodes[self.name]=(self,cost)

    def decouple(self,node):
        othernode=self.listNodes[node][0]
        del othernode.listNodes[self.name]
        del self.listNodes[node]

    def get_my_nodes(self):
        return [self.listNodes[x] for x in self.listNodes]


class GA():
    def __init__(self,population_size,mutation_probability,iteration_number):
        self.population_size=population_size
        self.mutation_probability=mutation_probability
        self.iteration_number=iteration_number
        self.population=[]

    def gen_individue(self):
        pass

    def crois(self,indiv1,indiv2):
        pass

    def fitness(self,ind):
        pass

    def muter(self,indiv):
        pass

    def tirer_indiv_alea(self):
        return self.population[random.randrange(len(self.population)-1)]

    def gen_initial_population(self):
        for i in range(0,self.population_size):
            self.population.append(self.gen_individue())

    def crois_population(self):
        for i in range(0,len(self.population)/2):
            ind1=self.tirer_indiv_alea()
            ind2=self.tirer_indiv_alea()
            (ind3,ind4)=self.crois(ind1,ind2)
            self.population.appen(ind3)
            self.population.appen(ind4)

    def mute_population(self):
        for i in self.population:
            r=random.random()
            if r < self.mutation_probability :
                self.population.remove(i)
                self.population.append(self.muter(i))

    def selection(self):
        newlist = sorted(self.population, key=lambda x: self.fitness(x), reverse=True)
        self.population=newlist[0:self.population_size]

    def start(self):
        gen_initial_population()
        for i in self.iteration_number:
            self.crois_population()
            self.mute_population()
            self.selection()
        return sorted(self.population, key=lambda x: self.fitness(x), reverse=True)[0]


class GA_altered(GA):
    global debug
    def gen_individue(self,graph,stopNode):
        # must remove visited nodes from possible nodes
        list_visited_nodes=[]

        currentNode=graph
        list_visited_nodes.append(currentNode)

        while(currentNode!=stopNode):
            possibleNodes=[x[0] for x in currentNode.listNodes.values()]
            if debug:
                print("list_visited_nodes",[x.name for x in list_visited_nodes],":",list_visited_nodes)
                print("possible nodes for :<",currentNode.name,">: ",possibleNodes)

            # for i in range(0,len(possibleNodes)):
            #     if possibleNodes[i] in list_visited_nodes
            #         del possibleNodes[i]
            currentNode=possibleNodes[random.randrange(0,len(possibleNodes))]
            list_visited_nodes.append(currentNode)
        if debug:
            print("list_visited_nodes",[x.name for x in list_visited_nodes],":",list_visited_nodes)
        return list_visited_nodes

    def crois(self,indiv1,indiv2):
        return (indiv1,indiv2)

    def fitness(self,indiv):
        # dont touch this shit
        somme=0
        basenode=indiv[0]
        for i in indiv[1::]:
            somme+=basenode.listNodes[i.name][1]
            basenode=basenode.listNodes[i.name][0]

        return somme

    def muter(self,indiv):
        return indiv




a=Node("a")
b=Node("b")
c=Node("c")
d=Node("d")

a.addNode(b,1)
a.addNode(c,1)

b.addNode(d,1)
c.addNode(d,1)

print("debug mode:",debug)
ga=GA_altered(10,10,10)
for i in range(0,10):
    print('indiv',i+1)
    indiv=ga.gen_individue(a,d)
    print(ga.fitness(indiv))

#dj kestra entre 2 point de ville
