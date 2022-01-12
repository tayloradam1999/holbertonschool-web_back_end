const { expect } = require('chai');
const mocha = require('mocha');


describe('Testing numbers', () => {
  it('1 is equal to 1', () => {
    expect(1 === 1).to.be.true;
  });

  it('2 is equal to 2', () => {
    expect(2 === 2).to.be.true;
  });

  // utilizes mocha's 'skip' to skip next test
  it.skip('1 is equal to 3', () => {
	expect(1 === 3).to.be.true;
  });

  // another way the above test could be written is as follows
  // xit('1 is equal to 3', () => {
	// expect(1 === 3).to.be.true;
  // });

  it('3 is equal to 3', () => {
    expect(3 === 3).to.be.true;
  });

  it('4 is equal to 4', () => {
    expect(4 === 4).to.be.true;
  });

  it('5 is equal to 5', () => {
    expect(5 === 5).to.be.true;
  });

  it('6 is equal to 6', () => {
    expect(6 === 6).to.be.true;
  });

  it('7 is equal to 7', () => {
    expect(7 === 7).to.be.true;
  });
});