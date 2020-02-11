import hashlib
from past.builtins import xrange
class MerckleTreeHash(object):
    def __init__(self):
        pass

    def find_merkle_hash(self,file_hashes):
        # We want to find the merkel tree hash of all the file hashes
        # passed to this function. Note we are going to be using recurssion
        # to solve this problem.
        # This is the simple procudure we will follow for finding the hash
        # given a list of hashes we first group all the hashes in twos
        # next we concatinate the hashes in each group and compute the hash
        # of group, then keep track of the group of the hashes. We will repeat
        # this steps until we have a single hash then that becomes the
        # hash we are looking for

        blocks = []

        if not file_hashes:
            raise ValueError('Missing require file hashes for computing merkle tree hash')

        # first sort the hashes
        for m in sorted(file_hashes):
            blocks.append(m)

        list_len = len(blocks)
        # Adjust block of hashes until we have an even number of items
        # in the blocks, this entails appending to the end of the block
        # the last entry. To do this we use modulus math to determine when
        # we have an even number of class
        while list_len % 2 != 0:
            blocks.extend(blocks[-1:])
            list_len = len(blocks)

        # Now we have an even number of items in the block we need to group
        # the items in twos

        secondary = []
        for k in [blocks[x:x+2] for x in xrange(0, len(blocks), 2)]:
            # Now because this is a recursive method
            # is so that we can concatinate them and create a new hash from
            # them 
            hasher = hashlib.sha256()
            hasher.update(k[0]+k[1])
            secondary.append(hasher.hexdigest())

            # Now because this is a recursive method, we need to determine
            # we only have a single item in the list that marks the end of the 
            # iteration and we can return the last hash as the merkel root

            if len(secondary) == 1:
                # Note i am only returning the first 64 charatecter, however if you want
                # want to return the entire hash just remove the last section
                # [0:64]
                return secondary[0][0:64]
            else:
                # If the number of items in the lists is more than one, we still
                # need to iterate through this so we pass it back to the
                # method. We pass the secondary list since it holds the second
                # iteration results
                return self.find_merkle_hash(secondary)

        if __name__== '__main__':
            # Will test by generating 13 random hashes and then try their
            # merkel tree hash
            import uuid
            file_hashes = []
            for _ in range(0,13):
                file_hashes.append(str(uuid.uuid4().hex))
            print ('Finding the merkel tree hash of {0} random hashes').format(
                len(file_hashes))
            cls = MerckleTreeHash()
            mk = cls.find_merkle_hash(file_hashes)
            print ('The merkle tree hash of the hashes below is: {0}').format(mk)
            print ('...')
            print (file_hashes)