

pragma solidity ^0.8.0;

contract Bank {
    mapping(address => uint) public balances;

    function depositMoney() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdrawMoney(uint amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;

        payable(msg.sender).transfer(amount);
    }

    function showbalance() public view returns (uint) {
        return balances[msg.sender];
    }
}
