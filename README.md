# Peer-to-Peer-File-Sharing-Application
Peer-to-Peer-File-Sharing-Application
A peer to peer file sharing application for CMP2204 Introduction to Computer Networks project.
This python program works with 4 processes: ChunkAnnouncer, ContentDiscovery, DownloadChunk and UploadChunk.

The file that will be transferred should be inside the python project file.
The user should change some parts of the python files.
- In the UploadChunk.py, user should change line 18 with own Hamachi IPv4 address.
- In the ContentDiscovery.py, user should change line 24 with own Hamachi IPv4 address.

First, you need to run ChunkAnnouncer.py and write the name of the file you want to upload (i.e., Bau.png). It will open a file called 'Chunk_Files' which contains 5 chunks. Then, you will write your username to the console. It will start to periodically send broadcast UDP message once per minute.
Next, you need to run UploadChunk.py in order to start server and upload the chunks.
Then, you need to run ContentDiscovery.py and it will create Users.txt file. In this file, you can see all chunks that are uploaded by users in the same network.
Finally, run DownloadChunk.py . In the console, you can see the files names shared in the network and ip adresses of senders. Write the name of the file (i.e., Bau.png) to the console. It will open a file called 'Downloads', which contains all files you download.

'Client_Success.log' file shows the chunks downloaded by you.
'Success.log' file shows the chunks available in the network.
