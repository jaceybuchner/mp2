#!/bin/bash

seeds=(1000 25 50 75 77 100 125 150 199 200 222 250 300 350 500 550 575 750 777 778)
total_percentage=0

for seed in "${seeds[@]}"; do
  output=$(python3 run_game.py --speed 10000 --seed $seed)
  percentage=$(echo "$output" | awk '/Percentage:/ {print $2}')
  echo "Seed $seed: Percentage: $percentage"
  total_percentage=$(echo "$total_percentage + $percentage" | bc)
done

average=$(echo "scale=2; $total_percentage / ${#seeds[@]}" | bc)
echo "Average Percentage: $average"
