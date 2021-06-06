pragma solidity ^0.8.4;

contract ETHContract { //contract's name 
    uint256 price; //private variable name token type unsigned int256
    constructor(uint256 _price) { //constructor run one time when deploy
        price = _price; 
    }
    
    // function for get eth price
    function GetEthPrice() public view returns(uint256) {
        return price;
    }
    
    // function for set eth price
    function SetEthPrice(uint256 _price) public{
        price = _price;
    }
}
