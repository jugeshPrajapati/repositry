import datetime
import hashlib
class BlockNew:
    blockNo=0
    data=None
    next=None
    nonce=0
    previous_hash=0*0
    timestamp=datetime.datetime.now()
    def __init__(self,data):
        self.data=data
    def hash(self):
        h=hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8')+str(self.data).encode('utf-8')+
            str(self.previous_hash).encode('utf-8')+str(self.timestamp).encode('utf-8')+
            str(self.blockNo).encode('utf-8')
            )
        return h.hexdigest()
    def __str__(self):
        return "\n block Hash:"+str(self.hash())+"\n block number:"+str(self.blockNo)+"\n date and time"+str(self.timestamp)+"\n previous hash:"+str(self.previous_hash)
class Blockchain:
    diff=20
    maxNonce=2**32
    target=2**(256-diff)
    block=BlockNew("genesis")
    #dummy=head=block
    def add(self,block):
        block.previous_hash=self.block.hash()
        block.blockNo=self.block.blockNo+1
        self.block.next=block
        self.block=self.block.next
    def mine(self,block):
        for n in range(self.maxNonce):
            if int(block.hash(),16)<=self.target:
                self.add(block)
                print(block,"\n nonce",n)
                break
            else:
                block.nonce+=1
blockchain1=Blockchain()
for n in range(10):
    blockchain1.mine(BlockNew("block mine"+str(n+1)))
    
    





























                
            
        
