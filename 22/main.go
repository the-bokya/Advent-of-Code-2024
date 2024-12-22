package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"strconv"
)

func main() {
	fileName := flag.String("file", "input", "Filename of input")
	flag.Parse()
	file, err := os.OpenFile(*fileName, os.O_RDONLY, 0644)
	if err != nil {
		fmt.Fprintln(os.Stderr, fmt.Errorf("File not found"))
		os.Exit(1)
	}
	buf := bufio.NewScanner(file)

	nums := make([]int, 0)

	for buf.Scan() {
		num, _ := strconv.Atoi(buf.Text())
		nums = append(nums, num)
	}
	fmt.Println("Part 1:", part1(nums))
}

func part1(nums []int) (count int) {
	for _, num := range nums {

		count += genSecretNth(num, 2000)
	}
	return count
}

func genSecret(num int) (secret int) {
	secret = num
	secret ^= (secret * 64)
	secret %= 16777216
	secret ^= (secret / 32)
	secret %= 16777216
	secret ^= secret * 2048
	secret %= 16777216
	return secret
}

func genSecretNth(num, n int) int {
	currentSecret := num
	for range n {
		currentSecret = genSecret(currentSecret)
	}
	return currentSecret
}
func genSecretSequence(num, n int) []int {
	secrets := make([]int, n)
	currentSecret := num
	for i := range n {
		currentSecret = genSecret(currentSecret)
		secrets[i] = currentSecret
	}
	return secrets
}
