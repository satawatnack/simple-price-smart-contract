pragma solidity ^0.8.4;

contract CoinContract {
    mapping(string => uint) prices;
     
    constructor(string memory name, uint256 _price) {
        prices[name] = _price; 
    }
    
    // function for get price
    function GetPriceByName(string memory name) public view returns(uint256) {
        return prices[name];
    }
    
    // function for set price
    function SePriceByName(string calldata name, uint256 _price) public{
        prices[name] = _price;
    }
}
