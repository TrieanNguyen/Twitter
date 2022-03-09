FROM ubuntu
MAINTAINER 18133006@student.hcmute.edu.vn
RUN apt update && apt install -y openssh-server openssh-client vim openjdk-11-jdk
RUN apt update && apt install -y git

# SSH
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
RUN sed -ri 's/#   StrictHostKeyChecking ask/    StrictHostKeyChecking accept-new/g' /etc/ssh/ssh_config
RUN chmod 0600 ~/.ssh/authorized_keys

RUN echo "root:123" | chpasswd
RUN echo "root   ALL=(ALL)       ALL" >> /etc/sudoers

ENV JAVA_HOME /usr/lib/jvm/java-1.11.0-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH

# HADOOP
RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-2.7.7/hadoop-2.7.7.tar.gz
RUN tar -xzf hadoop-2.7.7.tar.gz
RUN mv hadoop-2.7.7 usr/local/hadoop
ENV HADOOP_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop
ENV PATH $HADOOP_HOME/sbin:$PATH


ADD config/core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
ADD config/hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml
ADD config/mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml
ADD config/yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml
ADD config/slaves $HADOOP_HOME/etc/hadoop/slaves

RUN echo "export JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh
ENV PATH $HADOOP_HOME/bin:$PATH

#SCALA
RUN wget https://downloads.lightbend.com/scala/2.12.10/scala-2.12.10.deb
RUN dpkg -i scala-2.12.10.deb
RUN apt update && apt install -y scala

#SPARK 
RUN wget https://downloads.apache.org/spark/spark-3.0.3/spark-3.0.3-bin-hadoop2.7.tgz
RUN tar xvf spark-*
RUN mv spark-3.0.3-bin-hadoop2.7 usr/local/spark
ENV SPARK_HOME /usr/local/spark
ENV PATH $SPARK_HOME/bin:$PATH
ENV PATH $SPARK_HOME/sbin:$PATH
ENV PYSPARK_PYTHON usr/bin/python3

#LUIGI
RUN apt install -y python3-pip && pip install luigi
#RUN pip install hdfs

#CRON
RUN apt install -y cron

#CONFIG
ADD config/spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf
#ENV LB_LIBRARY_PATH=$HADOOP_HOME/lib/native:$LB_LIBRARY_PATH
#ADD Luigi/main.py job/main.py
ADD Cron/job-cron.txt job/cron-job.txt
#ADD Luigi/luigi.cfg job/luigi.cfg
ADD CreateData/main.py job/createData/main.py

#ADD JOB TO CRONTAB
RUN crontab /job/cron-job.txt
RUN touch /job/cron.log

#LUIGI STATE
RUN touch /tmp/luigi-state-file-8084
ADD Luigi/luigi.cfg job/luigi.cfg

#UPDATE scala
RUN apt remove -y scala-library scala
RUN wget https://downloads.lightbend.com/scala/2.11.12/scala-2.11.12.deb
RUN dpkg -i scala-2.11.12.deb
RUN apt update && apt install -y scala


#mysql-connector
RUN wget http://ftp.ntu.edu.tw/MySQL/Downloads/Connector-J/mysql-connector-java-8.0.26.tar.gz
RUN tar -xvf mysql-connector-java-8.0.26.tar.gz
RUN cp mysql-connector-java-8.0.26/mysql-connector-java-8.0.26.jar $HIVE_HOME/lib/

ADD config/hive-site.xml $SPARK_HOME/conf/
RUN cp mysql-connector-java-8.0.26/mysql-connector-java-8.0.26.jar $SPARK_HOME/jars/

#python package
RUN apt install -y python3-mysql.connector
RUN pip3 install pandas
RUN pip3 install findspark
RUN pip3 install textblob

ENV PYSPARK_PYTHON /usr/bin/python3

ARG FORMAT_NAMENODE_COMMAND
RUN $FORMAT_NAMENODE_COMMAND

CMD ["/usr/sbin/sshd", "-D"]

