class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

class LinkedList {
	constructor() {
		this.head = null;
		this.tail = null;
	}

	add(value) {
		const node = new Node(value);

		if (this.head) {
			this.tail.next = node;
		} else {
			this.head = node;
		}

		this.tail = node;
	}

	prepend(value) {
		const node = new Node(value);

		node.next = this.head;
		this.head = node;

		if (!this.tail)
			this.tail = node;
	}

	contains(value) {
		let currentNode = this.head;

		while (currentNode && currentNode.value !== value)
			currentNode = currentNode.next;

		return !!currentNode;
	}

	remove(value) {
		let previousNode = this.head;
		let currentNode = this.head;
		let count = 0;

		while (currentNode && currentNode.value !== value) {
			previousNode = currentNode;
			currentNode = currentNode.next;
			count++;
		}

		if (!currentNode)
			return false;

		if (count == 0) {
			this.head = this.head.next;

			return true;
		}

		previousNode.next = currentNode.next;

		return true;
	}

	get traverse() {
		return function* () {
			let currentNode = this.head;

			while (currentNode) {
				yield currentNode.value;
				currentNode = currentNode.next;
			}
		}
	}
}

// Basic Testing
const list = new LinkedList();

list.add(1);
list.prepend(2);
list.add(4);
list.remove(4);
list.remove(2);

let currentNode = list.head;
let count = 0;

while (currentNode) {
	console.log(`${count}: ${currentNode.value}`);

	currentNode = currentNode.next;
	count++;
}

console.log(`Contains 3?`, list.contains(3));
console.log(`Contains 2?`, list.contains(2));

let iterator = list.traverse();

console.log(iterator.next().value);