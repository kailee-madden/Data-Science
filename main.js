const SHA256 = require('crypto-js/sha256')

class Transaction{ //create a Transaction class 
    constructor(fromAddress, toAddress, amount){ //create constructor and its necessary parts
        this.fromAddress = fromAddress;
        this.toAddress = toAddress;
        this.amount = amount;
    }
}

class Block{ //create a Block class
    constructor(timestamp, transactions, previousHash = ''){ //create constructor and its necessary parts
        this.timestamp = timestamp;
        this.transactions = transactions;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
        this.nonce = 0; //a random number that doesn't have anything to do with the block but can be added for proof of work purposes
    }

    calculateHash(){ //calculate hash function, uses the other parts of the constructor
        return SHA256(this.previousHash + this.timestamp + JSON.stringify(this.transactions) + this.nonce).toString();
    }

    //a proof of work function
    mineBlock(difficulty){ //prevents tampering, looping through until get lucky and have enough zeros in the hash
        //cannot control where/when zeros appear in the hash so this requires a lot of computing power to loop until have adequate zeros
        //because it requires a high amount of computing power it prevents tampering and people from adding blocks that shouldn't be added
        while(this.hash.substring(0, difficulty) !== Array(difficulty+1).join("0")){ //difficulty is set in the Blockchain class that calls this function
            this.nonce++; //add to nonce until we have the correct number of zeros, more zeros means longer and more processing power needed
            this.hash = this.calculateHash();
        }
        console.log("Block mined: " + this.hash); //print to the console what the block is now that we mined it
    }
}

class Blockchain{ //create a Blockchain class
    constructor(){
        this.chain = [this.createOriginalBlock()]; //call the function to create the first block in the blockchain
        this.difficulty = 2; //by upping the difficulty can control how quickly new blocks can be added
        this.pendingTransactions = [];
        this.miningReward = 100;
    }

    createOriginalBlock(){ //function to create the first block in the blockchain
        return new Block(Date.parse("1996-11-10"), [], "0"); //set the conditions of the first block in the blockchain
    }

    getLatestBlock(){ //function to look at the most recent block in the blockchain
        return this.chain[this.chain.length - 1]; //length minus one since starts at 0
    }

    minePendingTransactions(miningRewardAddress){ //function to mine pending transactions by adding pending transactions to the new block that is then mined
        let block = new Block(Date.now(), this.pendingTransactions, this.getLatestBlock().hash); //adding all pending transactions isn't possible in real world scenarios, have to choose instead
        block.mineBlock(this.difficulty);

        console.log('The block was successfully mined.');
        this.chain.push(block); //once mined add the block to the rest of the chain

        this.pendingTransactions = [ //add the new transaction to pending transactions since it has to be validated before it goes through
            new Transaction(null, miningRewardAddress, this.miningReward)
        ];
    }

    createTransaction(transaction){ //function to push the created transaction to pending transactions
        this.pendingTransactions.push(transaction);
    }

    getBalanceOfAddress(address){ //function to get the balance of a particular address
        let balance = 0;

        for(const block of this.chain){ //loop through the blocks
            for(const trans of block.transactions){ //loop through the transactions in each block
                if(trans.fromAddress == address){ //check to see if the address matches the one associated with the transaction
                    balance -= trans.amount; //if so add or subtract the transaction amount to/from the balance
                }
                if(trans.toAddress == address){
                    balance += trans.amount;
                }
            }
        }
        return balance;
    }

    validchain(){ //function to test if the blockchain is valid and every block points to the previous block's hash
        for(let i =1; i< this.chain.length; i++){ //for loop to check all the blocks in the blockchain
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i-1];
            
            //check if the block's hash is what it is supposed to be and if the stored previous hash point's to the previous block's actual hash
            if(currentBlock.hash !== currentBlock.calculateHash() || currentBlock.previousHash !== previousBlock.hash){
                return false; 
            }
            //check if the block was mined properly and has the correct number of zeros
            if(currentBlock.hash.substring(0, this.mining_difficulty) !== "0".repeat(this.mining_difficulty)){
                return false;
        }
        }
        return true;
    }
}

let testBlockchain = new Blockchain(); //create a new blockchain
testBlockchain.createTransaction(new Transaction('address1', 'address2', 100)); //create new transactions
testBlockchain.createTransaction(new Transaction('address2', 'address1', 50));

console.log('\n Starting the miner ...');
testBlockchain.minePendingTransactions('kailees-address'); //mine the transactions

console.log('\n Balance of kailee is', testBlockchain.getBalanceOfAddress('kailees-address')); //check the address' balance
//the address will still have a balance of 0 since the transaction must be mined again in order to be validated and pushed through

console.log('\n Starting the miner again...');
testBlockchain.minePendingTransactions('kailees-address');

console.log('\n Balance of kailee is ', testBlockchain.getBalanceOfAddress('kailees-address')); //now the balance will be 100