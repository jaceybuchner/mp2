#!/bin/bash

seeds=(10 25 50 75 77 100 125 150 199 200 500 750 1000)
total_percentage=0

for seed in "${seeds[@]}"; do
  output=$(python3 run_game.py --speed 100 --seed $seed)
  percentage=$(echo "$output" | awk '/Percentage:/ {print $2}')
  echo "Seed $seed: Percentage: $percentage"
  total_percentage=$(echo "$total_percentage + $percentage" | bc)
done

average=$(echo "scale=2; $total_percentage / ${#seeds[@]}" | bc)
echo "Average Percentage: $average"
