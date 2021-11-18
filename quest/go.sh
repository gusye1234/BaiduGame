# export LD_LIBRARY_PATH=/home/gus/miniconda3/pkgs/cudnn-7.6.5-cuda10.1_0/lib:/home/gus/miniconda3/envs/tensorflow/lib:/usr/local/cuda/lib64:$LD_LIBRARY_PATH
# echo $LD_LIBRARY_PATH
python -u train.py \
       --train_set ../data/aug_train.txt \
       --dev_set ../data/dev.txt \
       --device gpu \
       --eval_step 2000 \
       --save_dir ./checkpoints \
       --train_batch_size 32 \
       --learning_rate 2E-5 \
       --rdrop_coef 0.0
                 