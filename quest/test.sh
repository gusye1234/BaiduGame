python -u \
    predict.py \
    --device gpu \
    --params_path "./checkpoints/model_47600/model_state.pdparams" \
    --batch_size 128 \
    --input_file ../data/test_A.tsv \
    --result_file "predict_result"