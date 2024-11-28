describe('Gerenciar Estoque de Insumos e Produtos (', () => {
  
  before(() => {
    cy.exec('python ./create_superuser.py');
    cy.visit('/');
    cy.contains('Cadastro').click();
    cy.get('input[name="email"]').type('teste@teste.com');
    cy.get('input[name="username"]').type('usuarioTeste');
    cy.get('input[name="full_Name"]').type('Jorginho Silva');
    cy.get('input[name="cpf"]').type('12345678901');
    cy.get('input[name="phone_number"]').type('+5581912345678');
    cy.get('input[name="street"]').type('Cais do Apolo');
    cy.get('input[name="home_number"]').type('123');
    cy.get('input[name="city"]').type('Recife');
    cy.get('input[name="state"]').type('PE');
    cy.get('input[name="country"]').type('Brasil');
    cy.get('input[name="password"]').type('senha123');
    cy.get('input[name="confirm_password"]').type('senha123');
    cy.get('button[type="submit"]').click();
  });

  beforeEach(() => {
    cy.contains('ARMAZENAMENTO').click({ force: true });
  });

  it('Adicionando um produto e editando esse produto', () => {
    cy.contains('Adicionar Produto').should('be.visible').click({ force: true });
    cy.get('#product_name').type('Semente de Soja', { force: true });
    cy.get('#category').select('Semente', { force: true });
    cy.get('#culture').select('Nenhuma', { force: true });
    cy.get('#quantity').type('500', { force: true });
    cy.get('#unit').select('kg', { force: true });
    cy.get('#average_cost').type('20.50', { force: true });
    cy.get('#recommended_area').type('2.0', { force: true });
    cy.get('.btn-submit').click({ force: true });
    cy.contains('Editar').should('be.visible').click({ force: true });
    cy.get('#product_name').clear().type('Semente de Milho', { force: true });
    cy.get('#quantity').clear().type('600', { force: true }); 
    cy.get('.btn-submit').click({ force: true });
});

after(() => {
  cy.visit('/admin/', { force: true });
  cy.get('#id_username').type('admin@admin.com', { force: true });
  cy.get('#id_password').type('admin123', { force: true });
  cy.get('.submit-row > input').click({ force: true });
  cy.contains('Users').click({ force: true });
  cy.get('#searchbar').type('teste@teste.com', { force: true });
  cy.get('#changelist-search > div > [type="submit"]').click({ force: true });
  cy.contains('teste@teste.com').should('be.visible', { force: true });
  cy.get('.action-select').click({ force: true });
  cy.get('select').select('Delete selected users', { force: true });
  cy.get('.button').click({ force: true });
  cy.get('div > [type="submit"]').click({ force: true });
});

});
