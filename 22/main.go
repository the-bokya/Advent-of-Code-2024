package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"strconv"
)

type Counter map[int]int

type PricePriceDiff struct {
	Price     int
	PriceDiff int
}

func (c Counter) Add(add Counter) {
	for k := range c {
		c[k] += add[k]
		delete(add, k)
	}
	for k := range add {
		c[k] += add[k]
	}
}

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
	fmt.Println("Part 2:", part2(nums))
}

func part1(nums []int) (count int) {
	for _, num := range nums {

		count += genSecretNth(num, 2000)
	}
	return count
}

func part2(nums []int) int {
	counter := make(Counter)
	for _, num := range nums {
		seq := genSecretSequence(num, 2000)
		prices := genPrices(num, seq)
		pmap := priceRangeMap(prices)
		counter.Add(pmap)
	}
	out := 0
	for _, v := range counter {
		out = max(out, v)
	}
	return out
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

func genPrices(initPrice int, nums []int) []PricePriceDiff {
	out := make([]PricePriceDiff, len(nums))
	prevPrice := initPrice % 10
	for i, num := range nums {
		var current PricePriceDiff
		current.Price = num % 10
		current.PriceDiff = current.Price - prevPrice
		out[i] = current
		prevPrice = current.Price
	}
	return out
}

func priceRangeMap(prices []PricePriceDiff) Counter {
	out := make(Counter)
	for i := range len(prices) - 3 {
		//unique key generation through base 20 (cuz negative numbers too)
		var key int
		mult := 1
		for j := range 4 {
			key += (prices[i+j].PriceDiff + 10) * mult
			mult *= 20
		}
		price := prices[i+3].Price
		_, ok := out[key]
		if !ok {
			out[key] = price
		}
	}
	return out
}
