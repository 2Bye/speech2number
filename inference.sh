echo "input csv: $1";
echo "ouput csv: $2";

python asr.py --input_csv $1

cd text2num

python t2n.py --output_csv $2

echo "Done"
echo "See your results in examples/{output_csv}"
cd ../
