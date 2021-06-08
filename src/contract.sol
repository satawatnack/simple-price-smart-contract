pragma solidity ^0.8.4;

contract CoinContract {
     struct Coin {
        uint rid;
        uint price;
    }
    mapping(string => Coin) coins;
     
    // function for get price
    function GetPriceByName(string memory name) public view returns(uint, uint) {
        return (coins[name].rid, coins[name].price);
    }
    
    // function for set price
    function SetPriceByName(uint _rid, string memory name, uint _price) public {
        Coin storage coin = coins[name];
        coin.price = _price;
        coin.rid = _rid;
    }
}
