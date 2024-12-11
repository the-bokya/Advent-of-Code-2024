package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func stoner(inp map[int]int) map[int]int {
	out := make(map[int]int)
	for k, v := range inp {
		for _, stone := range stoneStep(k) {
			out[stone] += v
		}
	}
	return out
}
func stoneStep(inp int) []int {
	out := make([]int, 0)
	if inp == 0 {
		out = append(out, 1)
		return out
	}
	s := strconv.Itoa(inp)
	l := len(s)
	if l%2 == 0 {
		a, _ := strconv.Atoi(s[:l/2])
		b, _ := strconv.Atoi(s[l/2:])
		out = append(out, a)
		out = append(out, b)
		return out
	}
	out = append(out, 2024*inp)
	return out

}
func main() {
	buf := bufio.NewScanner(os.Stdin)
	buf.Scan()
	numsStr := buf.Text()
	nums := make([]int, 0)
	for _, numStr := range strings.Split(numsStr, " ") {
		num, _ := strconv.Atoi(numStr)
		nums = append(nums, num)
	}
	numsMap := make(map[int]int)
	for _, num := range nums {
		numsMap[num] = 1
	}
	for _ = range 75 {
		numsMap = stoner(numsMap)
	}
	count := 0
	for _, v := range numsMap {
		count += v
	}
	fmt.Println(count)
}
