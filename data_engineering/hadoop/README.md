# Namenode
![](https://i.ibb.co/34fQWnm/image.png)

___

# Datanode
![](https://i.ibb.co/Hzf9PDv/image.png)

___

# Cluster metrics
![](https://i.ibb.co/Y3Y9hC4/image.png)

___

# App logs

22/06/06 13:07:15 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
22/06/06 13:07:16 INFO SparkContext: Running Spark version 3.1.1
22/06/06 13:07:16 INFO ResourceUtils: ==============================================================
22/06/06 13:07:16 INFO ResourceUtils: No custom resources configured for spark.driver.
22/06/06 13:07:16 INFO ResourceUtils: ==============================================================
22/06/06 13:07:16 INFO SparkContext: Submitted application: Simple Example
22/06/06 13:07:16 INFO ResourceProfile: Default ResourceProfile created, executor resources: Map(cores -> name: cores, amount: 1, script: , vendor: , memory -> name: memory, amount: 1024, script: , vendor: , offHeap -> name: offHeap, amount: 0, script: , vendor: ), task resources: Map(cpus -> name: cpus, amount: 1.0)
22/06/06 13:07:16 INFO ResourceProfile: Limiting resource is cpus at 1 tasks per executor
22/06/06 13:07:16 INFO ResourceProfileManager: Added ResourceProfile id: 0
22/06/06 13:07:16 INFO SecurityManager: Changing view acls to: root
22/06/06 13:07:16 INFO SecurityManager: Changing modify acls to: root
22/06/06 13:07:16 INFO SecurityManager: Changing view acls groups to:
22/06/06 13:07:16 INFO SecurityManager: Changing modify acls groups to:
22/06/06 13:07:16 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users  with view permissions: Set(root); groups with view permissions: Set(); users  with modify permissions: Set(root); groups with modify permissions: Set()
22/06/06 13:07:16 INFO Utils: Successfully started service 'sparkDriver' on port 34983.
22/06/06 13:07:16 INFO SparkEnv: Registering MapOutputTracker
22/06/06 13:07:16 INFO SparkEnv: Registering BlockManagerMaster
22/06/06 13:07:16 INFO BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
22/06/06 13:07:16 INFO BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up
22/06/06 13:07:16 INFO SparkEnv: Registering BlockManagerMasterHeartbeat
22/06/06 13:07:16 INFO DiskBlockManager: Created local directory at /tmp/blockmgr-ba148ef5-2a6e-40c6-b809-ddbc54b6047c
22/06/06 13:07:16 INFO MemoryStore: MemoryStore started with capacity 366.3 MiB
22/06/06 13:07:16 INFO SparkEnv: Registering OutputCommitCoordinator
22/06/06 13:07:16 INFO Utils: Successfully started service 'SparkUI' on port 4040.
22/06/06 13:07:16 INFO SparkUI: Bound SparkUI to 0.0.0.0, and started at http://4c5971cb9b02:4040
22/06/06 13:07:16 INFO RMProxy: Connecting to ResourceManager at resourcemanager/172.23.0.4:8032
22/06/06 13:07:17 INFO Client: Requesting a new application from cluster with 1 NodeManagers
22/06/06 13:07:17 INFO Configuration: resource-types.xml not found
22/06/06 13:07:17 INFO ResourceUtils: Unable to find 'resource-types.xml'.
22/06/06 13:07:17 INFO Client: Verifying our application has not requested more than the maximum memory capability of the cluster (8192 MB per container)
22/06/06 13:07:17 INFO Client: Will allocate AM container, with 896 MB memory including 384 MB overhead
22/06/06 13:07:17 INFO Client: Setting up container launch context for our AM
22/06/06 13:07:17 INFO Client: Setting up the launch environment for our AM container
22/06/06 13:07:17 INFO Client: Preparing resources for our AM container
22/06/06 13:07:17 WARN Client: Neither spark.yarn.jars nor spark.yarn.archive is set, falling back to uploading libraries under SPARK_HOME.
22/06/06 13:07:18 INFO Client: Uploading resource file:/tmp/spark-c1d14b48-59cb-49f8-ad5a-fdbdf7798786/__spark_libs__8544826188179294518.zip -> hdfs://namenode:9000/user/root/.sparkStaging/application_1654520062942_0001/__spark_libs__8544826188179294518.zip
22/06/06 13:07:19 INFO Client: Uploading resource file:/spark/python/lib/pyspark.zip -> hdfs://namenode:9000/user/root/.sparkStaging/application_1654520062942_0001/pyspark.zip
22/06/06 13:07:19 INFO Client: Uploading resource file:/spark/python/lib/py4j-0.10.9-src.zip -> hdfs://namenode:9000/user/root/.sparkStaging/application_1654520062942_0001/py4j-0.10.9-src.zip
22/06/06 13:07:19 INFO Client: Uploading resource file:/tmp/spark-c1d14b48-59cb-49f8-ad5a-fdbdf7798786/__spark_conf__3361672003428010252.zip -> hdfs://namenode:9000/user/root/.sparkStaging/application_1654520062942_0001/__spark_conf__.zip
22/06/06 13:07:20 INFO SecurityManager: Changing view acls to: root
22/06/06 13:07:20 INFO SecurityManager: Changing modify acls to: root
22/06/06 13:07:20 INFO SecurityManager: Changing view acls groups to:
22/06/06 13:07:20 INFO SecurityManager: Changing modify acls groups to:
22/06/06 13:07:20 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users  with view permissions: Set(root); groups with view permissions: Set(); users  with modify permissions: Set(root); groups with modify permissions: Set()
22/06/06 13:07:20 INFO Client: Submitting application application_1654520062942_0001 to ResourceManager
22/06/06 13:07:20 INFO YarnClientImpl: Submitted application application_1654520062942_0001
22/06/06 13:07:21 INFO Client: Application report for application_1654520062942_0001 (state: ACCEPTED)
22/06/06 13:07:21 INFO Client:
         client token: N/A
         diagnostics: AM container is launched, waiting for AM container to Register with RM
         ApplicationMaster host: N/A
         ApplicationMaster RPC port: -1
         queue: default
         start time: 1654520840406
         final status: UNDEFINED
         tracking URL: http://resourcemanager:8088/proxy/application_1654520062942_0001/
         user: root
22/06/06 13:07:22 INFO Client: Application report for application_1654520062942_0001 (state: ACCEPTED)
22/06/06 13:07:23 INFO Client: Application report for application_1654520062942_0001 (state: ACCEPTED)
22/06/06 13:07:24 INFO YarnClientSchedulerBackend: Add WebUI Filter. org.apache.hadoop.yarn.server.webproxy.amfilter.AmIpFilter, Map(PROXY_HOSTS -> resourcemanager, PROXY_URI_BASES -> http://resourcemanager:8088/proxy/application_1654520062942_0001), /proxy/application_1654520062942_0001
22/06/06 13:07:24 INFO YarnSchedulerBackend$YarnSchedulerEndpoint: ApplicationMaster registered as NettyRpcEndpointRef(spark-client://YarnAM)
22/06/06 13:07:24 INFO Client: Application report for application_1654520062942_0001 (state: RUNNING)
22/06/06 13:07:24 INFO Client:
         client token: N/A
         diagnostics: N/A
         ApplicationMaster host: 172.23.0.5
         ApplicationMaster RPC port: -1
         queue: default
         start time: 1654520840406
         final status: UNDEFINED
         tracking URL: http://resourcemanager:8088/proxy/application_1654520062942_0001/
         user: root
22/06/06 13:07:24 INFO YarnClientSchedulerBackend: Application application_1654520062942_0001 has started running.
22/06/06 13:07:24 INFO Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService' on port 45275.
22/06/06 13:07:24 INFO NettyBlockTransferService: Server created on 4c5971cb9b02:45275
22/06/06 13:07:24 INFO BlockManager: Using org.apache.spark.storage.RandomBlockReplicationPolicy for block replication policy
22/06/06 13:07:24 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, 4c5971cb9b02, 45275, None)
22/06/06 13:07:24 INFO BlockManagerMasterEndpoint: Registering block manager 4c5971cb9b02:45275 with 366.3 MiB RAM, BlockManagerId(driver, 4c5971cb9b02, 45275, None)
22/06/06 13:07:24 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(driver, 4c5971cb9b02, 45275, None)
22/06/06 13:07:24 INFO BlockManager: Initialized BlockManager: BlockManagerId(driver, 4c5971cb9b02, 45275, None)
22/06/06 13:07:25 INFO ServerInfo: Adding filter to /metrics/json: org.apache.hadoop.yarn.server.webproxy.amfilter.AmIpFilter
22/06/06 13:07:27 INFO YarnSchedulerBackend$YarnDriverEndpoint: Registered executor NettyRpcEndpointRef(spark-client://Executor) (172.23.0.5:56448) with ID 1,  ResourceProfileId 0
22/06/06 13:07:27 INFO BlockManagerMasterEndpoint: Registering block manager c4d0c5a90528:38425 with 366.3 MiB RAM, BlockManagerId(1, c4d0c5a90528, 38425, None)
22/06/06 13:07:27 INFO YarnSchedulerBackend$YarnDriverEndpoint: Registered executor NettyRpcEndpointRef(spark-client://Executor) (172.23.0.5:56452) with ID 2,  ResourceProfileId 0
22/06/06 13:07:27 INFO BlockManagerMasterEndpoint: Registering block manager c4d0c5a90528:35167 with 366.3 MiB RAM, BlockManagerId(2, c4d0c5a90528, 35167, None)
22/06/06 13:07:27 INFO YarnClientSchedulerBackend: SchedulerBackend is ready for scheduling beginning after reached minRegisteredResourcesRatio: 0.8
22/06/06 13:07:28 INFO SharedState: Setting hive.metastore.warehouse.dir ('null') to the value of spark.sql.warehouse.dir ('file:/spark-warehouse').
22/06/06 13:07:28 INFO SharedState: Warehouse path is 'file:/spark-warehouse'.
22/06/06 13:07:28 INFO ServerInfo: Adding filter to /SQL: org.apache.hadoop.yarn.server.webproxy.amfilter.AmIpFilter
22/06/06 13:07:28 INFO ServerInfo: Adding filter to /SQL/json: org.apache.hadoop.yarn.server.webproxy.amfilter.AmIpFilter
22/06/06 13:07:28 INFO ServerInfo: Adding filter to /SQL/execution: org.apache.hadoop.yarn.server.webproxy.amfilter.AmIpFilter
22/06/06 13:07:28 INFO ServerInfo: Adding filter to /SQL/execution/json: org.apache.hadoop.yarn.server.webproxy.amfilter.AmIpFilter
22/06/06 13:07:28 INFO ServerInfo: Adding filter to /static/sql: org.apache.hadoop.yarn.server.webproxy.amfilter.AmIpFilter
22/06/06 13:07:28 INFO InMemoryFileIndex: It took 28 ms to list leaf files for 1 paths.
22/06/06 13:07:28 INFO InMemoryFileIndex: It took 3 ms to list leaf files for 1 paths.
22/06/06 13:07:30 INFO FileSourceStrategy: Pushed Filters:
22/06/06 13:07:30 INFO FileSourceStrategy: Post-Scan Filters: (length(trim(value#0, None)) > 0)
22/06/06 13:07:30 INFO FileSourceStrategy: Output Data Schema: struct<value: string>
22/06/06 13:07:30 INFO CodeGenerator: Code generated in 128.938311 ms
22/06/06 13:07:30 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 304.8 KiB, free 366.0 MiB)
22/06/06 13:07:30 INFO MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 27.8 KiB, free 366.0 MiB)
22/06/06 13:07:30 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on 4c5971cb9b02:45275 (size: 27.8 KiB, free: 366.3 MiB)
22/06/06 13:07:30 INFO SparkContext: Created broadcast 0 from csv at NativeMethodAccessorImpl.java:0
22/06/06 13:07:30 INFO FileSourceScanExec: Planning scan with bin packing, max size: 7704589 bytes, open cost is considered as scanning 4194304 bytes.
22/06/06 13:07:30 INFO SparkContext: Starting job: csv at NativeMethodAccessorImpl.java:0
22/06/06 13:07:30 INFO DAGScheduler: Got job 0 (csv at NativeMethodAccessorImpl.java:0) with 1 output partitions
22/06/06 13:07:30 INFO DAGScheduler: Final stage: ResultStage 0 (csv at NativeMethodAccessorImpl.java:0)
22/06/06 13:07:30 INFO DAGScheduler: Parents of final stage: List()
22/06/06 13:07:30 INFO DAGScheduler: Missing parents: List()
22/06/06 13:07:30 INFO DAGScheduler: Submitting ResultStage 0 (MapPartitionsRDD[3] at csv at NativeMethodAccessorImpl.java:0), which has no missing parents
22/06/06 13:07:30 INFO MemoryStore: Block broadcast_1 stored as values in memory (estimated size 10.8 KiB, free 366.0 MiB)
22/06/06 13:07:30 INFO MemoryStore: Block broadcast_1_piece0 stored as bytes in memory (estimated size 5.4 KiB, free 366.0 MiB)
22/06/06 13:07:30 INFO BlockManagerInfo: Added broadcast_1_piece0 in memory on 4c5971cb9b02:45275 (size: 5.4 KiB, free: 366.3 MiB)
22/06/06 13:07:30 INFO SparkContext: Created broadcast 1 from broadcast at DAGScheduler.scala:1383
22/06/06 13:07:30 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 0 (MapPartitionsRDD[3] at csv at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
22/06/06 13:07:30 INFO YarnScheduler: Adding task set 0.0 with 1 tasks resource profile 0
22/06/06 13:07:30 INFO TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0) (c4d0c5a90528, executor 1, partition 0, RACK_LOCAL, 4879 bytes) taskResourceAssignments Map()
22/06/06 13:07:31 INFO BlockManagerInfo: Added broadcast_1_piece0 in memory on c4d0c5a90528:38425 (size: 5.4 KiB, free: 366.3 MiB)
22/06/06 13:07:31 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on c4d0c5a90528:38425 (size: 27.8 KiB, free: 366.3 MiB)
22/06/06 13:07:32 INFO TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 1275 ms on c4d0c5a90528 (executor 1) (1/1)
22/06/06 13:07:32 INFO YarnScheduler: Removed TaskSet 0.0, whose tasks have all completed, from pool
22/06/06 13:07:32 INFO DAGScheduler: ResultStage 0 (csv at NativeMethodAccessorImpl.java:0) finished in 1.352 s
22/06/06 13:07:32 INFO DAGScheduler: Job 0 is finished. Cancelling potential speculative or zombie tasks for this job
22/06/06 13:07:32 INFO YarnScheduler: Killing all running tasks in stage 0: Stage finished
22/06/06 13:07:32 INFO DAGScheduler: Job 0 finished: csv at NativeMethodAccessorImpl.java:0, took 1.386852 s
22/06/06 13:07:32 INFO CodeGenerator: Code generated in 7.416923 ms
22/06/06 13:07:32 INFO FileSourceStrategy: Pushed Filters:
22/06/06 13:07:32 INFO FileSourceStrategy: Post-Scan Filters:
22/06/06 13:07:32 INFO FileSourceStrategy: Output Data Schema: struct<value: string>
22/06/06 13:07:32 INFO MemoryStore: Block broadcast_2 stored as values in memory (estimated size 304.8 KiB, free 365.7 MiB)
22/06/06 13:07:32 INFO MemoryStore: Block broadcast_2_piece0 stored as bytes in memory (estimated size 27.8 KiB, free 365.6 MiB)
22/06/06 13:07:32 INFO BlockManagerInfo: Added broadcast_2_piece0 in memory on 4c5971cb9b02:45275 (size: 27.8 KiB, free: 366.2 MiB)
22/06/06 13:07:32 INFO SparkContext: Created broadcast 2 from csv at NativeMethodAccessorImpl.java:0
22/06/06 13:07:32 INFO FileSourceScanExec: Planning scan with bin packing, max size: 7704589 bytes, open cost is considered as scanning 4194304 bytes.
22/06/06 13:07:32 INFO FileSourceStrategy: Pushed Filters:
22/06/06 13:07:32 INFO FileSourceStrategy: Post-Scan Filters:
22/06/06 13:07:32 INFO FileSourceStrategy: Output Data Schema: struct<Country/Region: string, icon: string>
22/06/06 13:07:32 INFO FileOutputCommitter: File Output Committer Algorithm version is 1
22/06/06 13:07:32 INFO FileOutputCommitter: FileOutputCommitter skip cleanup _temporary folders under output directory:false, ignore cleanup failures: false
22/06/06 13:07:32 INFO SQLHadoopMapReduceCommitProtocol: Using output committer class org.apache.hadoop.mapreduce.lib.output.FileOutputCommitter
22/06/06 13:07:32 INFO CodeGenerator: Code generated in 20.399889 ms
22/06/06 13:07:32 INFO CodeGenerator: Code generated in 37.761492 ms
22/06/06 13:07:32 INFO MemoryStore: Block broadcast_3 stored as values in memory (estimated size 304.7 KiB, free 365.3 MiB)
22/06/06 13:07:32 INFO MemoryStore: Block broadcast_3_piece0 stored as bytes in memory (estimated size 27.7 KiB, free 365.3 MiB)
22/06/06 13:07:32 INFO BlockManagerInfo: Added broadcast_3_piece0 in memory on 4c5971cb9b02:45275 (size: 27.7 KiB, free: 366.2 MiB)
22/06/06 13:07:32 INFO SparkContext: Created broadcast 3 from csv at NativeMethodAccessorImpl.java:0
22/06/06 13:07:32 INFO FileSourceScanExec: Planning scan with bin packing, max size: 7704589 bytes, open cost is considered as scanning 4194304 bytes.
22/06/06 13:07:32 INFO BlockManagerInfo: Removed broadcast_1_piece0 on 4c5971cb9b02:45275 in memory (size: 5.4 KiB, free: 366.2 MiB)
22/06/06 13:07:32 INFO BlockManagerInfo: Removed broadcast_1_piece0 on c4d0c5a90528:38425 in memory (size: 5.4 KiB, free: 366.3 MiB)
22/06/06 13:07:32 INFO SparkContext: Starting job: csv at NativeMethodAccessorImpl.java:0
22/06/06 13:07:32 INFO DAGScheduler: Registering RDD 13 (csv at NativeMethodAccessorImpl.java:0) as input to shuffle 0
22/06/06 13:07:32 INFO DAGScheduler: Got job 1 (csv at NativeMethodAccessorImpl.java:0) with 1 output partitions
22/06/06 13:07:32 INFO DAGScheduler: Final stage: ResultStage 2 (csv at NativeMethodAccessorImpl.java:0)
22/06/06 13:07:32 INFO DAGScheduler: Parents of final stage: List(ShuffleMapStage 1)
22/06/06 13:07:32 INFO DAGScheduler: Missing parents: List(ShuffleMapStage 1)
22/06/06 13:07:32 INFO DAGScheduler: Submitting ShuffleMapStage 1 (MapPartitionsRDD[13] at csv at NativeMethodAccessorImpl.java:0), which has no missing parents
22/06/06 13:07:32 INFO MemoryStore: Block broadcast_4 stored as values in memory (estimated size 30.5 KiB, free 365.3 MiB)
22/06/06 13:07:32 INFO MemoryStore: Block broadcast_4_piece0 stored as bytes in memory (estimated size 14.1 KiB, free 365.3 MiB)
22/06/06 13:07:32 INFO BlockManagerInfo: Added broadcast_4_piece0 in memory on 4c5971cb9b02:45275 (size: 14.1 KiB, free: 366.2 MiB)
22/06/06 13:07:32 INFO SparkContext: Created broadcast 4 from broadcast at DAGScheduler.scala:1383
22/06/06 13:07:32 INFO DAGScheduler: Submitting 2 missing tasks from ShuffleMapStage 1 (MapPartitionsRDD[13] at csv at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1))
22/06/06 13:07:32 INFO YarnScheduler: Adding task set 1.0 with 2 tasks resource profile 0
22/06/06 13:07:32 INFO TaskSetManager: Starting task 0.0 in stage 1.0 (TID 1) (c4d0c5a90528, executor 2, partition 0, RACK_LOCAL, 4868 bytes) taskResourceAssignments Map()
22/06/06 13:07:32 INFO TaskSetManager: Starting task 1.0 in stage 1.0 (TID 2) (c4d0c5a90528, executor 1, partition 1, RACK_LOCAL, 4868 bytes) taskResourceAssignments Map()
22/06/06 13:07:32 INFO BlockManagerInfo: Added broadcast_4_piece0 in memory on c4d0c5a90528:38425 (size: 14.1 KiB, free: 366.3 MiB)
22/06/06 13:07:32 INFO BlockManagerInfo: Added broadcast_4_piece0 in memory on c4d0c5a90528:35167 (size: 14.1 KiB, free: 366.3 MiB)
22/06/06 13:07:32 INFO BlockManagerInfo: Added broadcast_3_piece0 in memory on c4d0c5a90528:38425 (size: 27.7 KiB, free: 366.2 MiB)
22/06/06 13:07:33 INFO TaskSetManager: Finished task 1.0 in stage 1.0 (TID 2) in 596 ms on c4d0c5a90528 (executor 1) (1/2)
22/06/06 13:07:33 INFO BlockManagerInfo: Added broadcast_3_piece0 in memory on c4d0c5a90528:35167 (size: 27.7 KiB, free: 366.3 MiB)
22/06/06 13:07:34 INFO TaskSetManager: Finished task 0.0 in stage 1.0 (TID 1) in 1779 ms on c4d0c5a90528 (executor 2) (2/2)
22/06/06 13:07:34 INFO YarnScheduler: Removed TaskSet 1.0, whose tasks have all completed, from pool
22/06/06 13:07:34 INFO DAGScheduler: ShuffleMapStage 1 (csv at NativeMethodAccessorImpl.java:0) finished in 1.787 s
22/06/06 13:07:34 INFO DAGScheduler: looking for newly runnable stages
22/06/06 13:07:34 INFO DAGScheduler: running: Set()
22/06/06 13:07:34 INFO DAGScheduler: waiting: Set(ResultStage 2)
22/06/06 13:07:34 INFO DAGScheduler: failed: Set()
22/06/06 13:07:34 INFO DAGScheduler: Submitting ResultStage 2 (CoalescedRDD[17] at csv at NativeMethodAccessorImpl.java:0), which has no missing parents
22/06/06 13:07:34 INFO MemoryStore: Block broadcast_5 stored as values in memory (estimated size 195.4 KiB, free 365.1 MiB)
22/06/06 13:07:34 INFO MemoryStore: Block broadcast_5_piece0 stored as bytes in memory (estimated size 72.5 KiB, free 365.0 MiB)
22/06/06 13:07:34 INFO BlockManagerInfo: Added broadcast_5_piece0 in memory on 4c5971cb9b02:45275 (size: 72.5 KiB, free: 366.1 MiB)
22/06/06 13:07:34 INFO SparkContext: Created broadcast 5 from broadcast at DAGScheduler.scala:1383
22/06/06 13:07:34 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 2 (CoalescedRDD[17] at csv at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
22/06/06 13:07:34 INFO YarnScheduler: Adding task set 2.0 with 1 tasks resource profile 0
22/06/06 13:07:34 INFO TaskSetManager: Starting task 0.0 in stage 2.0 (TID 3) (c4d0c5a90528, executor 2, partition 0, NODE_LOCAL, 10312 bytes) taskResourceAssignments Map()
22/06/06 13:07:34 INFO BlockManagerInfo: Added broadcast_5_piece0 in memory on c4d0c5a90528:35167 (size: 72.5 KiB, free: 366.2 MiB)
22/06/06 13:07:34 INFO MapOutputTrackerMasterEndpoint: Asked to send map output locations for shuffle 0 to 172.23.0.5:56452
22/06/06 13:07:35 INFO TaskSetManager: Finished task 0.0 in stage 2.0 (TID 3) in 750 ms on c4d0c5a90528 (executor 2) (1/1)
22/06/06 13:07:35 INFO YarnScheduler: Removed TaskSet 2.0, whose tasks have all completed, from pool
22/06/06 13:07:35 INFO DAGScheduler: ResultStage 2 (csv at NativeMethodAccessorImpl.java:0) finished in 0.768 s
22/06/06 13:07:35 INFO DAGScheduler: Job 1 is finished. Cancelling potential speculative or zombie tasks for this job
22/06/06 13:07:35 INFO YarnScheduler: Killing all running tasks in stage 2: Stage finished
22/06/06 13:07:35 INFO DAGScheduler: Job 1 finished: csv at NativeMethodAccessorImpl.java:0, took 2.571676 s
22/06/06 13:07:35 INFO FileFormatWriter: Write Job aff36000-5fdd-4349-91bd-608524c37228 committed.
22/06/06 13:07:35 INFO FileFormatWriter: Finished processing stats for write job aff36000-5fdd-4349-91bd-608524c37228.
22/06/06 13:07:35 INFO SparkContext: Invoking stop() from shutdown hook
22/06/06 13:07:35 INFO SparkUI: Stopped Spark web UI at http://4c5971cb9b02:4040
22/06/06 13:07:35 INFO YarnClientSchedulerBackend: Interrupting monitor thread
22/06/06 13:07:35 INFO YarnClientSchedulerBackend: Shutting down all executors
22/06/06 13:07:35 INFO YarnSchedulerBackend$YarnDriverEndpoint: Asking each executor to shut down
22/06/06 13:07:35 INFO YarnClientSchedulerBackend: YARN client scheduler backend Stopped
22/06/06 13:07:35 INFO MapOutputTrackerMasterEndpoint: MapOutputTrackerMasterEndpoint stopped!
22/06/06 13:07:35 WARN NioEventLoop: Selector.select() returned prematurely 512 times in a row; rebuilding Selector io.netty.channel.nio.SelectedSelectionKeySetSelector@53a6819.
22/06/06 13:07:35 INFO NioEventLoop: Migrated 0 channel(s) to the new Selector.
22/06/06 13:07:35 INFO MemoryStore: MemoryStore cleared
22/06/06 13:07:35 INFO BlockManager: BlockManager stopped
22/06/06 13:07:35 INFO BlockManagerMaster: BlockManagerMaster stopped
22/06/06 13:07:35 INFO OutputCommitCoordinator$OutputCommitCoordinatorEndpoint: OutputCommitCoordinator stopped!
22/06/06 13:07:35 INFO SparkContext: Successfully stopped SparkContext
22/06/06 13:07:35 INFO ShutdownHookManager: Shutdown hook called
22/06/06 13:07:35 INFO ShutdownHookManager: Deleting directory /tmp/spark-c1d14b48-59cb-49f8-ad5a-fdbdf7798786
22/06/06 13:07:35 INFO ShutdownHookManager: Deleting directory /tmp/spark-c1d14b48-59cb-49f8-ad5a-fdbdf7798786/pyspark-a6ef4f5b-febd-4789-a7cf-023a3192a8d4
22/06/06 13:07:35 INFO ShutdownHookManager: Deleting directory /tmp/spark-657d69d2-9e6e-4145-9cf4-d6f7ee8391bc
___
