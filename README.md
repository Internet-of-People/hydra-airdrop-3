Third Hydra Airdrop - 1 Million HYD
===================================

**UPDATE - Final Snapshots added**

Dear IOP Community, 
the data from the final snapshot is now online. The total amount of IOP coins recorded in the snapshots is 49741310.55187128 IOP over 13 days (about 3826254.62 IOP per day, excluding timelocked coins). This results in a reward of 0.020104013925 HYD per IOP for each day, or 0.261352181029 HYD for each IOP held over all snapshots. You can check the amount of HYD you can claim [here](src/data/processed/HYD_awarded.json). Registration will open on Saturday, April 21, at 3 PM UTC.  The registration will be open for exactly 1 week and closes on Saturday, April 28, at 3 PM (UTC). We will send out all HYD tokens after registration closes to save transaction cost.


**UPDATE - First 12 Snapshots added**

Dear IOP Community, 
we have now added the snapshot data for the first 12 days in the folder `src/data/snapshots_raw/` for everyone to compare. The last snapshot will be added tomorrow as planned, together with a table showing how much HYD can be claimed per address. Registration will open on Saturday, April 21, at 3 PM UTC.  The registration will be open for exactly 1 week and closes on Saturday, April 28, at 3 PM (UTC). Shortly after, you will receive your HYD tokens.


**UPDATE - Final Snapshot on Saturday, April 21**

Dear IOP Community, 
we have decided to release the Libertaria Exchange to the public on Saturday, April 21. On the same day, immediately after midnight, the last snapshot will be taken. In total we will then have made 13 snapshots. The registration will also open that day, approximately at 3 PM (UTC). The registration will be open for exactly 1 week and closes on Saturday, April 28 at 3 PM (UTC). Shortly after, you will receive your HYD tokens.

**Original Announcement**


Dear IOP Community,

Welcome to the third and final Hydra Airdrop. This time, up to 1 Million HYD tokens will be distributed. 

This time, we want to keep it simple. We care for only two things: How many IOP do you own, and how long will you hold it? Every IOP-satoshi will be rewarded with the same amount of HYD tokens, no matter how big the corresponding wallet is. Timelocked tokens and exchange wallets are again excluded.

We will start taking snapshots on the first block on Monday, April 9, 2018 (UTC). We will continue taking snapshots every day on the first block after midnight (UTC) until the release of the official Libertaria Exchanger. Every IOP held over the whole snapshot period will be rewarded with approximately 0.23 HYD (this number may change slightly depending on the total amount of IOP in existence at release time). Amounts held for fewer days will be rewarded accordingly, e.g. if you hold for half of the time, you will only get ~0.11 HYD per IOP.   

All snapshots are counted in total, so e.g. someone keeping 10 tokens for 5 days will get the same amount of HYD as someone keeping 5 Tokens for 10 days.

The process of claiming your airdrop is the same as always, detailed below. The registration will open after the final snapshot has been taken and the Libertaria Exchanger has been released.

**PLEASE NOTE**: It is vital that you store your IOP in a wallet that supports signing messages. We recommend using the official IoP Core Wallet, but the Coinomi Wallet for Android also works. Storing the IOP in the newly-released official IOP Android Wallet is in principle possible, but claiming your tokens will involve a more complicated process, so we cannot recommend at this time.


Claiming HYD Tokens
===================

To take part and receive your Hydra tokens, you need a valid Ethereum address **for which you control the private key**. You can register for the airdrop using the IoPCommunityBot in our official [Telegram Channel](https://t.me/IoPofficial). Please talk to the bot using private messages, to keep the channel clear for people asking questions. 

The command used for claiming an IOP address is `/%register YOUR_IOP_ADDRESS YOUR_ETH_ADDRESS SIGNATURE`. In this, `YOUR_IOP_ADDRESS` is the IOP address you want to claim and `YOUR_ETH_ADDRESS` is the address you want to receive the Hydra on. `SIGNATURE` is generated by using the *Sign Message* function of your IoP Core wallet. Enter your Ethereum address in the message field, without any other symbols or whitespace. Choose the IOP address you want to register and click *Sign*. Copy the resulting signature into the command for the telegram bot. This is used to verify that you indeed own the IOP address you want to register.

A very helpful video has already been uploaded to our official Internet of People YouTube Channel, explaining how to [register for the first Hydra Airdrop](https://youtu.be/hvMySKfQZ7Q). There is also a video explaining how to [register balances held in Coinomi Wallet](https://youtu.be/Hu6JHJPks30). The procedure is exactly the same for the second airdrop. The only difference is that the second airdrop is not a lottery, so the amount of tokens is already fixed when you register.

We also have a Java-based (works on Windows, Linux, MacOS...) command line tool to register all your addresses at once, including the ones the wallet doesn't show unless you run *listaddressgroupings*. It can be found [here](https://github.com/libertaria-project/hydra-airdrop-2/raw/master/src/register/jar/ClaimAirdrop.jar). To use it, see the steps listed [here](https://github.com/libertaria-project/hydra-airdrop-2/blob/master/src/register/jar/README.md). Please verify at least the MD5 hash of the jar. You can do this [here](http://onlinemd5.com) after downloading the jar.


I received fewer Hydras than expected
=====================================

If you find an address is credited with fewer Hydras than expected, please remember that your wallet generates change addresses every time you send a transaction. See [this article](https://iop.global/change-addresses/) for more information. Depending on their balance during the snapshot phases, these addresses might also be eligible. If you are using the official IOP Core Wallet, you can get a list of all addresses in your wallet--including change addresses--by running `listaddressgroupings` in the console found in your IoP Core Wallet under *Help->Debug Window->Console*. After registration closes, we will update this repository with the full registration data. 



# FAQ


If you still have questions, you should be able to find the answers here.

**Q**: What is an airdrop?
**A**: An airdrop is a distribution of free cryptocurrency to holders of a different currency. It’s a way to establish a broad base of token holders, reward a certain group of people or just generate buzz for a new token.

**Q**: Does it cost anything?
**A**: No, an airdrop is a free gift.

**Q**: Why is this airdrop happening? Who is it for?
**A**: To celebrate the long-standing partnership between IoP and Libertaria, Libertaria is rewarding members of the IoP community with a free gift of Hydra, Libertaria’s new cryptotoken.

**Q**: What is Hydra?
**A**: Hydra is Libertaria’s new cryptotoken. Eventually it will run on Libertaria’s new Hydra blockchain protocol, but for now it is an ERC20 token on the Ethereum blockchain. The address of the contract is 0xd233495c48eb0143661ffc8458eafc21b633f97f, the Token symbol is **HYD** and uses 12 digits.

**Q**: How many Hydra tokens are being airdropped?
**A**: 1,000,000 Hydra tokens are being distributed in this airdrop.

**Q**: Is everyone eligible to receive free Hydra tokens?
**A**: Every IOP addresses with a non-zero balance during the snapshoting phase (starting on Monday, April 9) is eligible to receive tokens in this airdrop.

**Q**: Will every eligible address receive free Hydra tokens?
**A**: Yes. The minimum amount each address will receive will be revealed here as soon as it is known.

**Q**: Can I receive Hydra from my IOP on Bittrex?
**A**: No, you cannot receive Hydra tokens based on Bittrex holdings. Only IOP addresses for which you own the private keys are eligible to register for the airdrop.

**Q**: What do I need to register my address?
**A**: You’ll need an eligible IOP address, an Ethereum wallet address for a wallet supporting ERC20 tokens and an IOP wallet capable of signing a message using the private key for the eligible IOP address. The official IoP Core wallet is perfect for this, exchange addresses are NOT. Another possibility is to use the Coinomi wallet.

**Q**: Which wallets support ERC20 tokens?
**A**: There are several options, but we recommend MyEtherWallet.com. We have created a short instructional video explaining how to set up a wallet address in MEW.

**Q**: How do I register my address?
**A**: You can register your address in our official IoP Token telegram channel by messaging our bot. The bot also accepts direct messages.

**Q**: The bot says I need a signature. What’s that?
**A**: We need a cryptographic signature to verify that you own the IoP address you’re trying to register. In your IoP core wallet, select “Sign Message” from the File menu. Paste the eligible IoP address in the top bar and your ETH address in the message box. Click the “Sign Message” button and the signature will be generated. You can use the Copy button to the right of the signature to copy it to the clipboard.

**Q**: The bot said: “That IoP address isn't on the list of IoP addresses eligible for this airdrop. Sorry.” Why?
**A**: Your tokens may have been stored in a different address than you think. Go to *Help->Debug Window->Console*, enter `listaddressgroupings` and hit return. The console window will display all the addresses your wallet used for your transactions. Check that list against the first list and you should find the tokens you’re looking for.

