package board

import (
	"testing"
)

func TestHello(t *testing.T) {
	friendly := hello()
	if !friendly {
		t.Errorf("Code is not being friendly! Expected true, got %t", friendly)
	}
}
