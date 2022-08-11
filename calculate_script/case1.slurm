#!/bin/bash
#SBATCH -J orca5_case             #作业名称
#SBATCH -p xhacnormalb                #指定队列名，网页平台"可访问队列"里面有队列名
#SBATCH -N 1                      #使用计算节点个数,跨节点一般需要调用mpi
#SBATCH --ntasks-per-node=4      #每个计算节点使用的核心数，上限是单个计算节点的所有核心数，多节点并行建议每个节点使用30核心并加上"#SBATCH --exclusive"参数
#SBATCH -o %j.log                 #指定作业的标准输出,%j是作业ID
#SBATCH -e %j.err                 #指定作业的报错输出,%j是作业ID

#加载环境变量
export PGI_FASTMATH_CPU=sandybridge
#g16 test.gjf 
for i in *single.gjf
do 
  g16 $i;
done
#g16 case1_s1_opt.gjf
