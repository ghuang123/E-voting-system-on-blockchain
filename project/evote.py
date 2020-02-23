from hashlib import *
#from cryptography.hazmat.primitives.asymmetric import *
import cryptography
from time import time

difficulty = 2

class vote:
    count = 0

    def __init__(self,candidateID):
        self.candidate = candidateID
        self.time = time()
        vote.count+=1
        Blockchain.votepool.append(self.__dict__)

class Blockchain:

    votepool = []
    chain = []

    @classmethod
    def __init__(cls):
        cls.length=len(cls.chain)

    def genesis(self):
        gen = Block(0,"Let the real democracy rule!!", sha256(str("Let the real democracy rule!!").encode('utf-8')).hexdigest(), difficulty, time(),'0')
        return gen

    def addGenesis(self):
        Blockchain.chain.append(self.genesis())

    def display(self):

        for block in self.chain:
            print("Block Height: ", block.height)
            print("Data in block: ", block.data)
            print("Merkle root: ", block.merkleRoot)
            print("Difficulty: ", block.difficulty)
            print("Time stamp: ", block.timeStamp)
            print("Previous hash: ", block.prevHash)
            print("Nonce: ", block.nonce)


class Block:

    def __init__(self,height,data,merkleRoot,difficulty,timeStamp,prevHash):
        self.height = height                   #len(Blockchain.chain-1)
        self.data = data                       #packdatainblock()
        self.merkleRoot = merkleRoot           #calculateMerkleRoot()
        self.difficulty = difficulty
        self.timeStamp = timeStamp             #time()
        self.prevHash = prevHash               #Blockchain.chain[len(Blockchain.chain)-1].hash
        self.nonce = self.pow()                # proof of work function will find nonce and hash will be found automatically. Return both values.

    def pow(self,zero=difficulty):
        self.nonce=0
        while(self.calcHash()[:zero]!='0'*zero):
            self.nonce+=1
        return self.nonce

    def calcHash(self):
        return sha256((str(str(self.data)+str(self.nonce)+str(self.timeStamp)+self.prevHash)).encode('utf-8')).hexdigest()

    def signvote(self):
        pass

    def loadvote(self):
        pass


if __name__=='__main__':

    EVoting = Blockchain()
    EVoting.addGenesis()
    EVoting.display()
