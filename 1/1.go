package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func abs(a int, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	as := make([]int, 0)
	bs := make([]int, 0)
	c := 0
	for {
		l, _, err := reader.ReadLine()
		if err != nil {
			break
		}
		c++
		nums := strings.Split(string(l), "   ")

		a, _ := strconv.Atoi(nums[0])
		b, _ := strconv.Atoi(nums[1])
		as = append(as, a)
		bs = append(bs, b)
	}
	slices.Sort(as)
	slices.Sort(bs)
	count := 0
	for i := range c {
		count += abs(as[i], bs[i])
	}
	fmt.Println(count)
}
