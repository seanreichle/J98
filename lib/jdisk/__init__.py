
"""
Aventesia Jarvis, JIOT 
================================================================================
Jarvis for CircuitPython on Ljinux
J-IOT
* Author(s): Sean C Reichle,..

Implementation Notes
jcloud - Cloud
#RAMDrive
--------------------
"""


import os

class jdisk():
    mountPath:str
    remaining:int
    
    class RAMBlockDev:
        def __init__(self, block_size, num_blocks):
            self.block_size = block_size
            self.data = bytearray(block_size * num_blocks)

        def readblocks(self, block_num, buf):
            for i in range(len(buf)):
                buf[i] = self.data[block_num * self.block_size + i]

        def writeblocks(self, block_num, buf):
            for i in range(len(buf)):
                self.data[block_num * self.block_size + i] = buf[i]

        def ioctl(self, op, arg):
            if op == 4: # get number of blocks
                return len(self.data) // self.block_size
            if op == 5: # get block size
                return self.block_size

    def __init__(self, somePath = "/tmp/ramdisk"):
        self.mountPath = somePath
        self.initStorage()

        
    def readOnly(self):
        self.readonly=False
        try:
            with open("/devm", "r") as f:
                self.readonly=True
        except:
            pass
            
        return self.readonly

    def storage(self):
        self.remaining = 0
        ds = os.statvfs(self.mountPath)
        '''
        Returns a tuple with the filesystem information in the following order:
        f_bsize – file system block size
        f_frsize – fragment size
        f_blocks – size of fs in f_frsize units
        f_bfree – number of free blocks
        f_bavail – number of free blocks for unpriviliged users
        f_files – number of inodes
        f_ffree – number of free inodes
        f_favail – number of free inodes for unpriviliged users
        f_flag – mount flags
        f_namemax – maximum filename length
        '''
        self.remaining = (ds[0] * (ds[3]))
        return self.remaining
        
    def initStorage(self, someSize=8):
        if not self.readOnly():
            try:
                self.mount_initrd(someSize, self.mountPath)
                return true
            except:
                pass
         
    def checkStorage(self):
        try:
            f=open(self.mountPath + '/info.txt', 'w')
            f.write("ok")        
            f.close()
        except:
            pass
        return open(self.mountPath + '/info.txt').read()
        
    def mount_initrd(num_blocks, path):
        try:      
            bdev = self.RAMBlockDev(512, num_blocks)
            os.VfsFat.mkfs(bdev)
            vfs = os.VfsFat(bdev)
            os.mount(vfs, path)
        except:
            pass